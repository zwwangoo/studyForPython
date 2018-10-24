"""
可同时匹配多种类型
"""
def test():
    try:
        raise KeyError('key')
    except (IndexError, KeyError) as exc:
        print(repr(exc), exc.__traceback__)


test()
