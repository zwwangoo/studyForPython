import zmq

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect('tcp://localhost:5557')

subscriber = context.socket(zmq.SUB)
subscriber.connect('tcp://localhost:5556')
subscriber.setsockopt(zmq.SUBSCRIBE, b'10001')

# Initialize poll set
poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(subscriber, zmq.POLLIN)

while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break
    if socks.get(receiver) == zmq.POLLIN:
        message = receiver.recv()
        print(message, 'receiver')
    if socks.get(subscriber) == zmq.POLLIN:
        message = subscriber.recv()
        print(message, 'subscriber')
