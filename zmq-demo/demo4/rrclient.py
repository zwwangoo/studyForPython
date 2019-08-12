import zmq

context = zmq.Context()

requester = context.socket(zmq.REQ)
requester.connect('tcp://localhost:5559')

for request_nbr in range(10):
    requester.send_string('Hello')
    s = requester.recv_string()
    print('Received response %d [%s]\n' % (request_nbr, s))

requester.close()
context.term()
