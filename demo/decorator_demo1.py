from functools import wraps


def log(fn):
    @wraps(fn)
    def wrap(*args, **kwargs):
        print(f"logs: {args}, {kwargs}")
        return fn(*args, **kwargs)
    return wrap


@log
def test(x: int, y: int) -> int:
    return x + y

test(2, 2)
