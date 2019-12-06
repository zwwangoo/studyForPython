from multiprocessing import Pool


def func_square(data):
    result = data * data
    return result


if __name__ == '__main__':
    inputs = list(range(100))
    pool = Pool(processes=4)
    pool_outputs = pool.map(func_square, inputs)
    pool.close()
    pool.join()
    print('Pool: ', pool_outputs)
