"""
桥接模式：将抽象部分与它的实现部分分离，使他们都可以独立的变化::

    >>> ab = RefinedAbstraction()
    >>> ab.implementor = ConcreteImplementorA()
    >>> ab.operation()
    具体实现A的方法执行。

    >>> ab.implementor = ConcreteImplementorB()
    >>> ab.operation()
    具体实现B的方法执行。
"""
import abc


class Implementor(abc.ABC):

    @abc.abstractmethod
    def operation(self): pass


class ConcreteImplementorA(Implementor):

    def operation(self):
        print('具体实现A的方法执行。')


class ConcreteImplementorB(Implementor):

    def operation(self):
        print('具体实现B的方法执行。')


class Abstracton(abc.ABC):
    def __init__(self):
        self.implementor = None

    @abc.abstractmethod
    def operation(self):
        self.implementor.operation()


class RefinedAbstraction(Abstracton):

    def operation(self):
        self.implementor.operation()


if __name__ == '__main__':
    ab = RefinedAbstraction()
    ab.implementor = ConcreteImplementorA()
    ab.operation()

    ab.implementor = ConcreteImplementorB()
    ab.operation()
