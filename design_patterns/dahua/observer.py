"""
观察者模式：定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主体对象。
这个主题对象在状态发生变化时，会通知所有的观察者对象，让它们能够自动更新自己::
    >>> s = ConcreteSubject()
    >>> s.attach(ConcreteObserver(s, 'X'))
    >>> s.attach(ConcreteObserver(s, 'Y'))
    >>> s.attach(ConcreteObserver(s, 'Z'))

    >>> s.subject_state = 'ABC'
    >>> s.notify()
    观察者X的新状态是ABC
    观察者Y的新状态是ABC
    观察者Z的新状态是ABC

当一个对象的改变需要同时改变其他对象的时候，且它不知道具体有多少对象有待改变时，
应该考虑使用观察者模式。

观察者模式所做的工作其实就是解除耦合，让耦合的双方都依赖抽象，而不是依赖于具体。
从而使得各自的变化都不会影响另一边的变化。是依赖倒转原则的最佳体现。

但是抽象通知者还是依赖抽象观察者。在代码中抽象观察者中有一个update()方法，具体
观察者中都要实现该方法，但是在实际中，可能有一些不一样的操作，根本就不是同名的
方法。这是不足的地方。
"""
import abc


class Subject:
    """抽象通知者"""

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class Observer(abc.ABC):
    """抽象观察者"""

    @abc.abstractmethod
    def update(self):
        pass


class ConcreteSubject(Subject):
    """具体通知者"""

    def __init__(self):
        self.subject_state = None
        super().__init__()


class ConcreteObserver(Observer):
    """具体观察者"""

    def __init__(self, subject, name):
        self.name = name
        self.subject = subject

    def update(self):
        observer_state = self.subject.subject_state
        print('观察者{0}的新状态是{1}'.format(self.name, observer_state))


if __name__ == '__main__':
    s = ConcreteSubject()
    s.attach(ConcreteObserver(s, 'X'))
    s.attach(ConcreteObserver(s, 'Y'))
    s.attach(ConcreteObserver(s, 'Z'))

    s.subject_state = 'ABC'
    s.notify()
