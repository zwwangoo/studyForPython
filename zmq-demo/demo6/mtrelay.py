'''
三个线程之间需要进行同步
'''

import threading
import zmq


def step1(context):
    xmitter = context.socket(zmq.PAIR)
    xmitter.connect('inproc://step2')
    print('step1 ok, setp2 ...')
    xmitter.send_string('READY')
    xmitter.close()


def step2(context):
    receiver = context.socket(zmq.PAIR)
    receiver.bind('inproc://step2')
    thread = threading.Thread(target=step1, args=(context,))
    thread.start()

    s = receiver.recv_string()
    print(s)
    receiver.close()

    xmitter = context.socket(zmq.PAIR)
    xmitter.connect('inproc://step3')
    print('step2 ok, step3...')
    xmitter.send_string('READY')
    xmitter.close()


def main():
    context = zmq.Context()
    receiver = context.socket(zmq.PAIR)
    receiver.bind('inproc://step3')
    thread = threading.Thread(target=step2, args=(context,))
    thread.start()

    s = receiver.recv_string()
    print(s)
    receiver.close()
    print('ok!')
    context.term()


if __name__ == '__main__':
    main()
