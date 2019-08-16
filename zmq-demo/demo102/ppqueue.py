from collections import OrderedDict

import time
import zmq

HEARTBEAT_LIVENESS = 3
HEARTBEAT_INTERVAL = 1.0

PPP_READY = b'\x01'  # 应答信号
PPP_HEARTBEAT = b'\x02'  # 心跳信号


class Worker:
    def __init__(self, address):
        self.address = address
        self.expiry = time.time() + HEARTBEAT_INTERVAL * HEARTBEAT_LIVENESS


class WorkerQueue:
    def __init__(self):
        self.queue = OrderedDict()

    def ready(self, worker):
        self.queue.pop(worker.address, None)
        self.queue[worker.address] = worker

    def purge(self):
        ''' 清理过期的worker '''
        now = time.time()
        expired = []
        for address, worker in self.queue.items():
            if now > worker.expiry:
                expired.append(address)
        for address in expired:
            print('W:Idle worker expired: %s' % address)
            self.queue.pop(address, None)

    def next(self):
        address, worker = self.queue.popitem(False)
        return address


context = zmq.Context()

frontend = context.socket(zmq.ROUTER)
frontend.bind('tcp://*:5555')
backend = context.socket(zmq.ROUTER)
backend.bind('tcp://*:5556')

poller_workers = zmq.Poller()
poller_workers.register(backend, zmq.POLLIN)

poller_both = zmq.Poller()
poller_both.register(frontend, zmq.POLLIN)
poller_both.register(backend, zmq.POLLIN)

workers = WorkerQueue()

heartbeat_at = time.time() + HEARTBEAT_INTERVAL

while True:
    if len(workers.queue) > 0:
        poller = poller_both
    else:
        poller = poller_workers
    socks = dict(poller.poll(HEARTBEAT_INTERVAL * 1000))
    if socks.get(backend) == zmq.POLLIN:
        msg = backend.recv_multipart()
        address, msg = msg[0], msg[1:]
        workers.ready(Worker(address))

        if msg[-1] not in [PPP_HEARTBEAT, PPP_READY]:
            frontend.send_multipart(msg)

    if socks.get(frontend) == zmq.POLLIN:
        msg = frontend.recv_multipart()
        if not msg:
            break
        msg = [workers.next()] + msg
        backend.send_multipart(msg)

    # 发送心跳给空闲的worker
    if time.time() > heartbeat_at:
        for worker in workers.queue:
            msg = [worker, PPP_HEARTBEAT]
            backend.send_multipart(msg)
        heartbeat_at = time.time() + HEARTBEAT_INTERVAL

    workers.purge()

backend.close()
frontend.close()
context.term()
