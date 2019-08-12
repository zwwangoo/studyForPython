import zmq

context = zmq.Context()
print('connecting to hello world server')
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for request in range(10):
    print("Sending request %s ..." % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
