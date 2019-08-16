import time
import zmq
from random import randint

HEARTBEAT_LIVENESS = 3
HEARTBEAT_INTERVAL = 1

INTERVAL_INIT = 1  # 重试间隔
INTERVAL_MAX = 32  # 回退算法最大值

#  Paranoid Pirate Protocol constants
PPP_READY = b'\x01'      # Signals worker is ready
PPP_HEARTBEAT = b'\x02'  # Signals worker heartbeat


def worker_socket(context, poller):
    worker = context.socket(zmq.DEALER)
    ident = (u'%04x-%04x' %
             (randint(0, 0x10000), randint(0, 0x10000))).encode()
    worker.setsockopt(zmq.IDENTITY, ident)
    worker.connect('tcp://localhost:5556')
    poller.register(worker, zmq.POLLIN)
    worker.send(PPP_READY)

    return worker


context = zmq.Context()
poller = zmq.Poller()

worker = worker_socket(context, poller)

liveness = HEARTBEAT_LIVENESS
interval = INTERVAL_INIT

heartbeat_at = time.time() + HEARTBEAT_INTERVAL

cycles = 0
while True:

    socks = dict(poller.poll(HEARTBEAT_INTERVAL * 1000))
    if socks.get(worker) == zmq.POLLIN:
        msg = worker.recv_multipart()
        if not msg:
            break

        if len(msg) == 3:
            # 3段消息，信封+内容，表示一个请求
            cycles += 1
            if cycles > 3 and randint(0, 9) == 0:
                print('模拟崩溃')
                break
            if cycles > 3 and randint(0, 9) == 0:
                print('模拟CPU过载')
                time.sleep(3)
            print('%s: 正常应答' % worker.identity)
            worker.send_multipart(msg)
            liveness = HEARTBEAT_LIVENESS
            time.sleep(1)
        elif len(msg) == 1 and msg[-1] == PPP_HEARTBEAT:
            print('队列装置心跳')
            liveness = HEARTBEAT_LIVENESS
        else:
            print('非法信息: %s') % msg
        interval = INTERVAL_INIT
    else:
        liveness -= 1
        if liveness == 0:
            print('心跳失败，无法连接队列装置')
            print('%0.2fs 毫秒后进行重连...' % interval)
            time.sleep(interval)

            if interval < INTERVAL_MAX:
                interval *= 2
            poller.unregister(worker)
            worker.setsockopt(zmq.LINGER, 0)
            worker.close()
            worker = worker_socket(context, poller)
            liveness = HEARTBEAT_LIVENESS
    if time.time() > heartbeat_at:
        heartbeat_at = time.time() + HEARTBEAT_INTERVAL
        worker.send(PPP_HEARTBEAT)
