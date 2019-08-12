import zmq
import time

context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect('tcp://localhost:5561')
subscriber.setsockopt(zmq.SUBSCRIBE, b'')

time.sleep(1)

syncclient = context.socket(zmq.REQ)
syncclient.connect('tcp://localhost:5562')

syncclient.send(b'')
print('等待信号')
s = syncclient.recv()

data_nbr = 0
while True:
    s = subscriber.recv_string()
    if s == 'END':
        break
    data_nbr += 1

print('%d' % data_nbr)
syncclient.close()
subscriber.close()
context.term()
