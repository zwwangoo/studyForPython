import time
import zmq

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind('tcp://*:5563')

while True:
    publisher.send_multipart([b"A", b"We don't want to see this"])
    publisher.send_multipart([b"B", b"We would like to see this"])
    time.sleep(1)

publisher.close()
context.term()
