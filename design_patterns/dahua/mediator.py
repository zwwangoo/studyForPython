"""
中介者模式：用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式的相
互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互::

    >>> m = ConcreteMediator()
    >>> c1 = ConcreteHandler1(m)
    >>> c2 = ConcreteHandler2(m)

    >>> m.colleague1 = c1
    >>> m.colleague2 = c2

    >>> c1.send('吃饭了吗？')
    同事2得到消息： 吃饭了吗？
    >>> c2.send('没有呢，你打算请客？')
    同事1得到消息： 没有呢，你打算请客？

"""
import abc


class Mediator(abc.ABC):
    """抽象中介者"""

    @abc.abstractmethod
    def send(self, message, colleague): pass


class Colleague(abc.ABC):
    """抽象同事类"""

    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print('{}得到消息：'.format(self.name), message)


class ConcreteMediator(Mediator):
    """具体中介者类"""

    def __init__(self):
        self.colleague1 = None
        self.colleague2 = None

    def send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.notify(message)
        else:
            self.colleague1.notify(message)


class ConcreteHandler1(Colleague):
    """同事类1"""

    def __init__(self, mediator):
        super().__init__(mediator)
        self.name = '同事1'


class ConcreteHandler2(Colleague):
    """同事类2"""

    def __init__(self, mediator):
        super().__init__(mediator)
        self.name = '同事2'


if __name__ == '__main__':
    m = ConcreteMediator()
    c1 = ConcreteHandler1(m)
    c2 = ConcreteHandler2(m)

    m.colleague1 = c1
    m.colleague2 = c2

    c1.send('吃饭了吗？')
    c2.send('没有呢，你打算请客？')
