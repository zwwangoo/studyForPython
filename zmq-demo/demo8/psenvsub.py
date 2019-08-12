import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect('tcp://localhost:5563')
subscriber.setsockopt(zmq.SUBSCRIBE, b'B')

while True:
    [addr, content] = subscriber.recv_multipart()
    print('%s, %s' % (addr, content))

subscriber.close()
context.term()
