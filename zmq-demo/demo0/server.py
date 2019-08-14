'''
基础的请求-应答模式。
REP 用于响应方，不能主动发送请求，必须是在有响应之后才可以应答。
'''
import time
import zmq

# 创建zmq上下文, 该上下文是线程安全的，可以在多线程中使用。
context = zmq.Context()
socket = context.socket(zmq.REP)
# 绑定套接字到端点
socket.bind("tcp://*:5555")

while True:
    # 等待客户端请求
    message = socket.revc()
    print("Received request: %s" % message)

    # 做些处理
    time.sleep(1)

    # 响应客户端
    socket.send(b"World")
