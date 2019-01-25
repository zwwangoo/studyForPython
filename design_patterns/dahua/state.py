"""
状态模式：当一个对象的内在状态改变时，允许改变其行为，这个对象看起来像是一个改变了其类::
    >>> c = Context(ConcreteStateA())
    >>> c.request()
    当前状态：stateB
    >>> c.request()
    当前状态：stateA
    >>> c.request()
    当前状态：stateB
    >>> c.request()
    当前状态：stateA
    >>> c.request()
    当前状态：stateB

状态模式主要解决的是当控制一个对象状态转换的条件表达式过于复杂时的情况，把状态的判断转移到表示不同状态的一系列类中可以把复杂的判断逻辑简化。

状态模式的好处是将与特定状态相关的行为局部化，并且将不同状态的行为分割开来。
"""
import abc


class State(abc.ABC):
    """抽象状态类，定义一个接口以封装一个特定状态相关的行为"""
    @abc.abstractmethod
    def headle(self, context):
        pass


class ConcreteStateA(State):
    """具体状态类"""
    def __init__(self):
        self.name = 'stateA'

    def headle(self, context):
        context.state = ConcreteStateB()


class ConcreteStateB(State):
    def __init__(self):
        self.name = 'stateB'

    def headle(self, context):
        context.state = ConcreteStateA()


class Context:
    """这个类的实例定义当前的状态。"""
    def __init__(self, state):
        """初始状态"""
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print('当前状态：{}'.format(self._state.name))

    def request(self):
        self.state.headle(self)


if __name__ == '__main__':
    c = Context(ConcreteStateA())

    c.request()
    c.request()
    c.request()
    c.request()
    c.request()
