import zmq
import random
import time

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind('tcp://*:5557')

print('Press Enter when the workers as ready:')
_ = input()
print('Sending tasks to workers...')

total_msec = 0
for task_nbr in range(100):
    workload = random.randint(1, 100)
    total_msec += workload

    sender.send_string(u'%i' % workload)

print('Total expected cost: %s msec' % total_msec)
time.sleep(1)
sender.close()
context.term()
