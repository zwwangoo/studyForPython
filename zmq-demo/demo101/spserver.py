from random import randint
import time
import zmq

context = zmq.Context()
server = context.socket(zmq.REQ)
ident = (u"%04X-%04X" % (randint(0, 0x10000), randint(0, 0x10000))).encode()
server.setsockopt(zmq.IDENTITY, ident)
server.connect('tcp://localhost:5556')

server.send(b'READY')

cycles = 0
while True:
    request = server.recv_multipart()
    if not request:
        break
    cycles += 1
    if cycles > 3 and randint(0, 3):
        print('%s:模拟程序崩溃' % ident)
        break
    elif cycles > 3 and randint(0, 3):
        print('%s: 模拟CPU过载' % ident)
        time.sleep(2)

    print('正常请求 %s' % request)
    time.sleep(1)
    server.send_multipart(request)

server.close()
context.term()
