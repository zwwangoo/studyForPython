import time
import random
import sys
import zmq


def main(myself, others):

    print('I: %s...' % myself)
    context = zmq.Context()
    statebe = context.socket(zmq.PUB)
    bind_addr = u'ipc://%s-state.ipc' % myself
    statebe.bind(bind_addr)

    statefe = context.socket(zmq.SUB)
    statefe.setsockopt(zmq.SUBSCRIBE, b'')
    for other in others:
        statefe.connect('ipc://%s-state.ipc' % other)
        time.sleep(1.0)

    poller = zmq.Poller()
    poller.register(statefe, zmq.POLLIN)

    while True:
        # poll 设定心跳时间
        socks = dict(poller.poll(1000))

        if socks.get(statefe) == zmq.POLLIN:
            msg = statefe.recv_multipart()
            print('%s Received: %s' % (myself, msg))
        else:
            # 发送随机数表示空闲的worker数
            msg = [bind_addr, (u'%i' % random.randrange(1, 10))]
            msg = [m.encode('ascii') for m in msg]
            statebe.send_multipart(msg)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1], sys.argv[2:])
    else:
        print('Usage: peering.py <myself> <peer_1> ... <peer_N>')
        sys.exit(1)
