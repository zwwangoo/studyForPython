"""
享元模式：运用共享技术有效地支持大量细粒度的对象::
    >>> extrinsicstate = 22
    >>> f = FlyweightFactory()
    >>> fx = f.get_flyweight('X')
    >>> fx.operation(extrinsicstate - 1)
    具体Flyweight: 21

    >>> fy = f.get_flyweight('Y')
    >>> fy.operation(extrinsicstate - 2)
    具体Flyweight: 20

    >>> uf = UnsharedConcreteFlyweight()
    >>> uf.operation(extrinsicstate - 3)
    不共享的具体Flyweight: 19

享元模式可以避免大量非常相似类的开销。在程序设计中，有时需要生成大量的细粒度的
类示例来表示数据，如果能够发现这些实例除了几个参数外基本上都相同的，有时就能够
受大幅度的减少需要实例化的类数量。如果把这些参数移到类实例的外面，在方法调用的
时候将它们传递进来，就可以通过共享大幅度的减少单个实例的数目。

应用场合：如果一个应用程序使用了大量的对象，而大量的这些对象造成了很大的存储开
销时，应该考虑使用，还有就是对象的大多数状态可以外部状态，如果删除对象的外部状
态，那么可以用相对较少的共享对象取代很多的组对象，此时可以考虑使用享元模式。
"""
import abc


class Flyweight(abc.ABC):

    @abc.abstractmethod
    def operation(self, extrinsicstate): pass


class ConcreteFlyweight(Flyweight):

    def operation(self, extrinsicstate):
        print('具体Flyweight:', extrinsicstate)


class UnsharedConcreteFlyweight(Flyweight):

    def operation(self, extrinsicstate):
        print('不共享的具体Flyweight:', extrinsicstate)


class FlyweightFactory:

    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if not self.flyweights.get(key, None):
            self.flyweights[key] = ConcreteFlyweight()
        return self.flyweights.get(key)


if __name__ == '__main__':
    extrinsicstate = 22
    f = FlyweightFactory()
    fx = f.get_flyweight('X')
    fx.operation(extrinsicstate - 1)

    fy = f.get_flyweight('Y')
    fy.operation(extrinsicstate - 2)

    uf = UnsharedConcreteFlyweight()
    uf.operation(extrinsicstate - 3)
