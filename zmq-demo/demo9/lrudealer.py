import zmq
import uuid
from threading import Thread
import time
import random


def get_uuid():
    return bytes(str(uuid.uuid4()), 'utf-8')


def worke_task():
    context = zmq.Context()
    worker = context.socket(zmq.REQ)
    uid = get_uuid()
    worker.setsockopt(zmq.IDENTITY, uid)
    worker.connect('ipc://routing.ipc')

    total = 0
    while True:
        worker.send(b'READY')

        msg = worker.recv()
        if msg == b'END':
            print('%s received %s' % (uid, total))
            break
        total += 1

        time.sleep(0.1 * random.random())
    worker.close()
    context.term()


def main():

    context = zmq.Context()
    client = context.socket(zmq.ROUTER)
    client.bind('ipc://routing.ipc')

    for i in range(10):
        Thread(target=worke_task).start()

    for i in range(100):
        addr, empty, ready = client.recv_multipart()
        client.send_multipart([addr, b'', b'This is workload'])

    for i in range(10):
        addr, empty, ready = client.recv_multipart()
        client.send_multipart([addr, b'', b'END'])
    client.close()
    context.term()


if __name__ == '__main__':
    main()
