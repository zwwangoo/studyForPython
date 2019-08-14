'''
worker收到自杀信号后便会中止
'''
import time
import sys
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect('tcp://localhost:5557')

sender = context.socket(zmq.PUSH)
sender.connect('tcp://localhost:5558')

controller = context.socket(zmq.SUB)
controller.connect('tcp://localhost:5559')
controller.setsockopt(zmq.SUBSCRIBE, b'')

poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(controller, zmq.POLLIN)

while True:

    socks = dict(poller.poll())

    if socks.get(receiver) == zmq.POLLIN:
        message = receiver.recv_string()

        workload = int(message)
        time.sleep(workload/1000.0)

        sender.send_string(message)

        sys.stdout.write('.')
        sys.stdout.flush()

    # 自杀信号
    if socks.get(controller) == zmq.POLLIN:
        msg = controller.recv()
        if msg == b'KILL':
            break

receiver.close()
sender.close()
controller.close()
context.term()
