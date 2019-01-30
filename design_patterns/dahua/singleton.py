"""
单例模式：保证一个类仅有一个实例，并提供一个访问它的全局访问点::
    >>>
    >>> singleton1 = Singleton('wen') # doctest: +ELLIPSIS
    单例：...
    >>> singleton2 = Singleton('wen1')  # doctest: +ELLIPSIS
    单例：...
    >>> print(singleton1 is singleton2)
    True

通常我们可以让一个全局变量使得一个对象被访问，但是它不能防止你实例化多个对象，
一个最好的办法就是：让类自身负责它的唯一实例。这个类可以保证没有其他的实例可以
被创建，并且它可以提供一个访问该实例的方法。

"""



class Singleton:
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        print('单例：', id(self))
        self.name = name

if __name__ == '__main__':
    singleton1 = Singleton('wen')
    singleton2 = Singleton('wen1')
    print(singleton1 is singleton2)
