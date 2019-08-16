import time
import random
import zmq

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind('tcp://*:5555')

cycles = 0
while True:
    cycles += 1
    if cycles > 3 and random.randint(0, 3):
        print('模拟程序崩溃')
        break
    elif cycles > 3 and random.randint(0, 3):
        print('模拟CPU过载')
        time.sleep(2)

    request = server.recv()
    print('正常请求 %s' % request)
    time.sleep(1)
    server.send(request)

server.close()
context.term()
