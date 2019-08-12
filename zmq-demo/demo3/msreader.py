import time
import zmq


context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect('tcp://localhost:5557')

subscriber = context.socket(zmq.SUB)
subscriber.connect('tcp://localhost:5556')
subscriber.setsockopt(zmq.SUBSCRIBE, b'10001')

while True:
    while True:
        try:
            msg = receiver.recv(zmq.DONTWAIT)
            print(msg, 'receiver')
        except zmq.Again:
            break

    while True:
        try:
            msg = subscriber.recv(zmq.DONTWAIT)
            print(msg, 'subscriber')
        except zmq.Again:
            break
    time.sleep(0.001)
