"""
迭代器模式：提供一种方法顺序访问一个聚合对象中各个元素，而不是暴露该对象的
内部表示。代码事例为乘务员迭代检票的模拟演示::
    >>> a = ConcreteAggregate()
    >>> a[0] = '大鸟'
    >>> a[1] = '小菜'
    >>> a[2] = '行李'
    >>> a[3] = '老外'
    >>> a[4] = '员工'
    >>> a[5] = '小偷'

    >>> i = ConcreteIterator(a)
    >>> item = i.first()
    >>> while not i.is_done():
    ...     print('{} 请买票!'.format(i.current_item()))
    ...     i.next()
    大鸟 请买票!
    小菜 请买票!
    行李 请买票!
    老外 请买票!
    员工 请买票!
    小偷 请买票!

为遍历不同的聚合结构提供如开始、下一个、是否结束、当前哪一项等统一的接口。现在
高级编程语言如C#、JAVA、Python等本身已经把这个模式做在语言中。
"""
import abc


class Iterator(abc.ABC):

    @abc.abstractmethod
    def first(self): pass

    @abc.abstractmethod
    def next(self): pass

    @abc.abstractmethod
    def is_done(self): pass

    @abc.abstractmethod
    def current_item(self): pass


class Aggregate(abc.ABC):
    @abc.abstractmethod
    def create_iterator(self): pass


class ConcreteIterator(Iterator):

    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current = 0

    def first(self):
        return self.aggregate[0]

    def next(self):
        self.current += 1

    def is_done(self):
        return self.current >= self.aggregate.count()

    def current_item(self):
        return self.aggregate[self.current]


class ConcreteAggregate(Aggregate):

    def __init__(self):
        self.items = {}

    def create_iterator(self):
        return ConcreteIterator(self)

    def count(self):
        return len(self.items)

    def __setitem__(self, index, value):
        self.items[index] = value

    def __getitem__(self, index):
        return self.items[index]


if __name__ == '__main__':
    a = ConcreteAggregate()
    a[0] = '大鸟'
    a[1] = '小菜'
    a[2] = '行李'
    a[3] = '老外'
    a[4] = '员工'
    a[5] = '小偷'

    i = ConcreteIterator(a)
    item = i.first()
    while not i.is_done():
        print(i.current_item(), '请买票!')
        i.next()
