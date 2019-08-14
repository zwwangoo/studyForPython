'''
拓展请求-应答模式，使用broker进行负载均衡。

REP(server)只需要和DEALER对话;
'''
import zmq

context = zmq.Context()
server = context.socket(zmq.REP)
server.connect('tcp://localhost:5561')

while True:
    msg = server.recv()
    print(msg)
    server.send(b'OK')
