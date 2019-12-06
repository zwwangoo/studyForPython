import multiprocessing


def foo(x):
    print('called function in process: %s' % x)
    return x * x


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()
        p.join()
