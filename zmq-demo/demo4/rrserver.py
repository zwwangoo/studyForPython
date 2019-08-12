import time
import zmq

context = zmq.Context()

responder = context.socket(zmq.REP)
responder.connect('tcp://localhost:5560')

while True:
    s = responder.recv_string()
    print('Received request:[%s]\n' % s)
    time.sleep(1)
    responder.send_string('World')
