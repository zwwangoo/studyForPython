"""
上下文的对象创建, 这里演示的借助了标准库contextlib
"""
import contextlib


@contextlib.contextmanager
def db_context(db):
    try:
        print(f'open: {db}')
        yield db
    finally:
        print(f'close: {db}')


def test(db):
    with db_context(db):
        print(f'exec {db}')
        raise Exception('error')


test('mysql')
