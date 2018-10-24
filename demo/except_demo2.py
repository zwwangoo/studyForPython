"""
使用raise抛出异常时，还可用from字句接收另一异常，形成链式结构
"""
def test():
    try:
        raise Exception('err')
    except Exception as exc:
        raise Exception('wrap') from exc


def main():
    try:
        test()
    except Exception as exc:
        while True:
            print(repr(exc), exc.__traceback__)
            if not exc.__cause__: break
            exc = exc.__cause__


if __name__ == '__main__':
    main()
