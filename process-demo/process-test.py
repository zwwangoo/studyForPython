import time
import random
import multiprocessing as mp

queue = mp.Queue(4)


def do_work():
    while True:
        item = queue.get()
        print(item)
        time.sleep(random.randint(1, 3))
        print(item, 'end')


def main():

    for i in range(4):
        proc = mp.Process(target=do_work)
        proc.start()

    while True:
        if queue.full():
            continue

        for c in 'abcdefg':
            if queue.full():
                break
            if random.choice([0, 1]):
                queue.put(c)


main()
