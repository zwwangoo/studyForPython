import threading
import time
import zmq


def worker_task_a():
    context = zmq.Context()
    worker = context.socket(zmq.DEALER)
    worker.setsockopt(zmq.IDENTITY, b'A')
    worker.connect('ipc://routing.ipc')

    total = 0
    while True:
        msg = worker.recv()
        if msg == b'END':
            print('A received %s' % total)
            break
        total += 1
    worker.close()
    context.term()


def worker_task_b():
    context = zmq.Context()
    worker = context.socket(zmq.DEALER)
    worker.setsockopt(zmq.IDENTITY, b'B')
    worker.connect('ipc://routing.ipc')

    total = 0
    while True:
        msg = worker.recv()
        if msg == b'END':
            print('B received %s' % total)
            break
        total += 1
    worker.close()
    context.term()


def main():

    context = zmq.Context()
    client = context.socket(zmq.ROUTER)
    client.bind('ipc://routing.ipc')

    threading.Thread(target=worker_task_a).start()
    threading.Thread(target=worker_task_b).start()

    time.sleep(1)

    for i in range(10):
        worlds = b'This is workload'
        if i < 3:
            worker = b'A'
        else:
            worker = b'B'
        client.send_multipart([worker, worlds])

    client.send_multipart([b'A', b'END'])
    client.send_multipart([b'B', b'END'])
    client.close()
    context.term()


if __name__ == '__main__':
    main()
