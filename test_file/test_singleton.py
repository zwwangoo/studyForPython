def singleton(cls, *args, **kw):
    instance = {}
    def get_singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return get_singleton


@singleton
class TT(object):
    def __init__(self):
        self.num = 0
    def add(self):
        self.num = 100


class A(object):
    def __init__(self):
        print('init A...')

    def getoo(self):
        print("getoo")


class B(object):
    def __init__(self):
        print('init B...')

    def demo(self):
        print("B")


class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('init C...')

    def demo(self):
        print("C")


class D(B):
    def __init__(self):
        super(D, self).__init__()
        print('init D...')


class E(D,C):
    def __init__(self):
        super(E, self).__init__()
        print('init E...')


if __name__ == '__main__':
    e = E()
    e.demo()
    e.getoo()
