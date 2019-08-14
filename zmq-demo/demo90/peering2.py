import time
import random
import sys
import zmq
from threading import Thread


def client_task(name, i):
    context = zmq.Context()
    client = context.socket(zmq.REQ)
    ident = (u'Client-%s-%s' % (name, i)).encode('ascii')
    client.setsockopt(zmq.IDENTITY, ident)
    client.connect('ipc://%s-localfe.ipc' % name)

    while True:
        # 发送请求，接收应答
        client.send(b'HELLO')
        try:
            reply = client.recv()
        except zmq.ZMQError:
            return
        print('Client-%s-%s: %s\n' % (name, i, reply))
        time.sleep(1)

    client.close()
    context.term()


def worker_task(name, i):

    context = zmq.Context()
    worker = context.socket(zmq.REQ)
    ident = (u'Worker-%s-%s' % (name, i)).encode('ascii')
    worker.setsockopt(zmq.IDENTITY, ident)
    worker.connect('ipc://%s-localbe.ipc' % name)
    worker.send(b'READY')

    while True:
        try:
            msg = worker.recv_multipart()
        except zmq.ZMQError:
            return

        print('Worker-%s-%s: %s\n' % (name, i, msg))
        msg[-1] = b'OK'
        # 注意这里发送的msg格式
        worker.send_multipart(msg)

    worker.close()
    context.term()


def main(myself, peers):
    print("I: preparing broker at %s..." % myself)

    context = zmq.Context()

    # 将cloudfe绑定至端点
    cloudfe = context.socket(zmq.ROUTER)
    if not isinstance(myself, bytes):
        ident = myself.encode('ascii')
    else:
        ident = myself
    cloudfe.setsockopt(zmq.IDENTITY, ident)
    cloudfe.bind('ipc://%s-cloud.ipc' % myself)

    # 将cloudbe连接至同代理的端点
    cloudbe = context.socket(zmq.ROUTER)
    cloudbe.setsockopt(zmq.IDENTITY, ident)
    for peer in peers:
        print("I: connecting to cloud frontend at %s" % peer)
        cloudbe.connect('ipc://%s-cloud.ipc' % peer)

    if not isinstance(peers[0], bytes):
        peers = [peer.encode('ascii') for peer in peers]

    # 准备本地localfe 和localbe
    localfe = context.socket(zmq.ROUTER)
    localfe.bind('ipc://%s-localfe.ipc' % myself)

    localbe = context.socket(zmq.ROUTER)
    localbe.bind('ipc://%s-localbe.ipc' % myself)

    _ = input()

    # 启动本地worker
    for i in range(10):
        t = Thread(target=worker_task, args=(myself, i))
        t.daemon = True
        t.start()

    # 启动本地client
    for i in range(3):
        t = Thread(target=client_task, args=(myself, i))
        t.daemon = True
        t.start()

    workers = []

    pollerbe = zmq.Poller()
    pollerbe.register(localbe, zmq.POLLIN)
    pollerbe.register(cloudbe, zmq.POLLIN)

    pollerfe = zmq.Poller()
    pollerfe.register(localfe, zmq.POLLIN)
    pollerfe.register(cloudfe, zmq.POLLIN)

    while True:
        try:
            events = dict(pollerbe.poll(1000 if workers else None))
        except zmq.ZMQError:
            break

        msg = None
        if events.get(localbe) == zmq.POLLIN:
            msg = localbe.recv_multipart()
            print('localbe ', msg)
            address, msg = msg[0], msg[2:]
            workers.append(address)

            # 如果是“已就绪”的信号，则不再进行路由
            if msg[-1] == b'READY':
                msg = None
        elif events.get(cloudbe) == zmq.POLLIN:
            msg = cloudbe.recv_multipart()
            address, msg = msg[0], msg[2:]

        if msg is not None:
            address = msg[0]
            if address in peers:
                cloudfe.send_multipart(msg)
            else:
                localfe.send_multipart(msg)

        while workers:
            events = dict(pollerfe.poll(0))
            reroutable = False
            if events.get(cloudfe) == zmq.POLLIN:
                msg = cloudfe.recv_multipart()
                reroutable = False
            elif events.get(localfe) == zmq.POLLIN:
                msg = localfe.recv_multipart()
                reroutable = True
            else:
                break  # 没有work

            if reroutable and peers and random.randint(0, 4) == 0:
                msg = [random.choice(peers), b''] + msg
                cloudbe.send_multipart(msg)
            else:  # 优先使用本地资源
                msg = [workers.pop(0), b''] + msg
                localbe.send_multipart(msg)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2:])
    else:
        print('Usage: peering.py <myself> <peer_1> ... <peer_N>')
        sys.exit(1)
