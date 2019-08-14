import time
import random
import sys
import zmq
from threading import Thread


def client_task(name, i):

    context = zmq.Context()
    client = context.socket(zmq.REQ)
    ident = (u'Client-%s-%i' % (name, i)).encode('ascii')
    client.setsockopt(zmq.IDENTITY, ident)
    client.connect('ipc://%s-localfe.ipc' % name)

    monitor = context.socket(zmq.PUSH)
    monitor.connect('ipc://%s-monitor.ipc' % name)

    poller = zmq.Poller()
    poller.register(client, zmq.POLLIN)
    while True:

        time.sleep(random.randint(0, 5))

        for _ in range(random.randint(0, 15)):
            # 生成随机的16进制id
            task_id = u"%04X" % random.randint(0, 10000)
            client.send_string(task_id)

            try:
                # 最多等待10秒
                events = dict(poller.poll(10000))
            except zmq.ZMQError:
                return
            if events.get(client) == zmq.POLLIN:
                reply = client.recv_string()
                assert reply == task_id, '%s !== %s' % (reply, task_id)
                monitor.send_string(reply)
            else:
                monitor.send_string('客户端任务丢失： %s' % task_id)


def worker_task(name, i):
    context = zmq.Context()
    worker = context.socket(zmq.REQ)
    ident = (u'Worker-%s-%s' % (name, i)).encode('ascii')
    worker.setsockopt(zmq.IDENTITY, ident)
    worker.connect('ipc://%s-localbe.ipc' % name)

    # 通知broker worker已经准备就绪
    worker.send(b'READY')

    while True:
        try:
            msg = worker.recv_multipart()
        except zmq.ZMQError:
            break
        time.sleep(random.randint(0, 1))
        worker.send_multipart(msg)

    worker.close()
    context.term()


def main(myself, peers):

    context = zmq.Context()
    cloudfe = context.socket(zmq.ROUTER)
    if not isinstance(myself, bytes):
        ident = myself.encode('ascii')
    else:
        ident = myself
    cloudfe.setsockopt(zmq.IDENTITY, ident)
    cloudfe.bind('ipc://%s-cloud.ipc' % myself)

    cloudbe = context.socket(zmq.ROUTER)
    cloudbe.setsockopt(zmq.IDENTITY, ident)
    # 将statebe绑定至端点
    statefe = context.socket(zmq.SUB)
    statefe.setsockopt(zmq.SUBSCRIBE, b'')
    statefe.setsockopt(zmq.IDENTITY, ident)
    for peer in peers:
        print("I: connecting to cloud frontend at %s" % peer)
        cloudbe.connect('ipc://%s-cloud.ipc' % peer)

        print('I: connecting to state frontend at %s' % peer)
        statefe.connect('ipc://%s-state.ipc' % peer)

    statebe = context.socket(zmq.PUB)
    statebe.bind('ipc://%s-state.ipc' % myself)

    localbe = context.socket(zmq.ROUTER)
    localbe.bind('ipc://%s-localbe.ipc' % myself)

    localfe = context.socket(zmq.ROUTER)
    localfe.bind('ipc://%s-localfe.ipc' % myself)

    # 准备监控套接字
    monitor = context.socket(zmq.PULL)
    monitor.bind('ipc://%s-monitor.ipc' % myself)

    _ = input()

    # 启动本地worker
    for i in range(10):
        t = Thread(target=worker_task, args=(myself, i))
        t.domain = True
        t.start()

    # 启动本地client
    for i in range(5):
        t = Thread(target=client_task, args=(myself, i))
        t.domain = True
        t.start()

    worker = []
    local_capacity = 0
    cloud_capacity = 0
    pollerbe = zmq.Poller()
    pollerbe.register(localbe, zmq.POLLIN)
    pollerbe.register(cloudbe, zmq.POLLIN)
    pollerbe.register(monitor, zmq.POLLIN)
    pollerbe.register(statebe, zmq.POLLIN)

    while True:
        try:
            events = dict(pollerbe.poll(1000 if worker else None))
        except zmq.ZMQError:
            break

        # 跟踪自身状态是否发生变化
        previous = local_capacity
        msg = None

        #  轮训后端套接字，从worker处获取应答或就绪消息

        if events.get(localbe) == zmq.POLLIN:
            msg = localbe.recv_multipart()
            address, msg = msg[0], msg[2:]
            worker.append(address)
            local_capacity += 1

            if msg[-1] == b'READY':
                msg = None
        elif events.get(cloudbe) == zmq.POLLIN:
            msg = cloudbe.recv_multipart()
            address, msg = msg[0], msg[2:]
        # 将应答发送
        if msg is not None:
            # 判断应答消息归属，并进行发送
            address = msg[0]
            if address in peers:
                cloudfe.send_multipart(msg)
            else:
                localfe.send_multipart(msg)

        # 处理监控信息
        if events.get(monitor) == zmq.POLLIN:
            status = monitor.recv_string()
            print('%s\n' % status)

        if events.get(statefe) == zmq.POLLIN:
            peer, status = statefe.recv_multipart()
            cloud_capacity = int(status)

        # 开始处理客户端请求

        while local_capacity + cloud_capacity:  # 有可用的worker
            pollerfe = zmq.Poller()
            pollerfe.register(localfe, zmq.POLLIN)
            if cloud_capacity > 0:
                pollerfe.register(cloudfe, zmq.POLLIN)

            try:
                events = dict(pollerfe.poll(0))
            except zmq.ZMQError:
                return
            if events.get(localfe) == zmq.POLLIN:
                msg = localfe.recv_multipart()
            elif events.get(cloudfe) == zmq.POLLIN:
                msg = cloudfe.recv_multipart()
            else:
                break

            if local_capacity:
                # 优先使用本地资源
                msg = [worker.pop(0), b''] + msg
                localbe.send_multipart(msg)
                local_capacity -= 1
            else:
                # 随机发送broker
                msg = [random.choice(peers), b''] + msg
                cloudbe.send_multipart(msg)
        # 广播状态，本地有剩余worker
        if local_capacity != previous:
            # 信息地址指向自己
            statebe.send_multipart(
                [ident, str(local_capacity).encode('ascii')],
            )


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2:])
    else:
        print('Usage: peering.py <myself> <peer_1> ... <peer_N>')
