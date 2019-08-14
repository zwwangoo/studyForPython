'''
基础的请求-应答模式。
REQ 用于请求方，如果没有应答将一直等待。
'''
import zmq

context = zmq.Context()
print('connecting to hello world server')
socket = context.socket(zmq.REQ)
# 连接套接字到端点
socket.connect('tcp://localhost:5555')

for request in range(10):
    # 主动发送请求
    print("Sending request %s ..." % request)
    socket.send(b"Hello")

    # 等待响应
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
