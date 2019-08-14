'''
拓展请求-应答模式，使用broker进行负载均衡。

REQ(client)只需要和ROUTER对话;
'''
import time
import zmq


context = zmq.Context()

client = context.socket(zmq.REQ)
client.connect('tcp://localhost:5560')

while True:
    client.send(b'HELLO')
    msg = client.recv()
    print(msg)
    time.sleep(3)
