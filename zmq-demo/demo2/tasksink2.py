import time
import sys
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind('tcp://*:5558')

controller = context.socket(zmq.PUB)
controller.bind('tcp://*:5559')

string = receiver.recv()
tstart = time.time()

for task_nbr in range(100):
    string = receiver.recv()
    if task_nbr % 10 == 0:
        sys.stdout.write('\n:')
    else:
        sys.stdout.write('.')

    sys.stdout.flush()

tend = time.time()
print('Total elapsed time: %d msec' % ((tend - tstart) * 1000))

controller.send(b'KILL')
receiver.close()
controller.close()
context.term()
