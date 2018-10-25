def log(fn):
    def wrap(*args, **kwargs):
        print(f'log: {args}, {kwargs}')
        return fn(*args, **kwargs)
    return wrap


@log
def test(x, y):
    return x + y


test(2, 3)
