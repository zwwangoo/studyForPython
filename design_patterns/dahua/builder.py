"""
建造者模式：将一个复杂对象的构建与它的表示分离，是的同样的构建过程，可以创建不同的表示::
    >>> director = Director()
    >>> b1 = ConcreateBuilder1()
    >>> b2 = ConcreateBuilder2()

    >>> director.construct(b1)
    >>> p1 = b1.get_result()
    >>> p1.show()
    产品 创建 ----
    部件A
    部件B

    >>> director.construct(b2)
    >>> p2 = b2.get_result()
    >>> p2.show()
    产品 创建 ----
    部件X
    部件Y

建造者模式是当常见复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时使用的模式。

如果我们用了建造者模式，那么用户就只需指定需要建造的类型就可以得到他们，而具体建造的过程
和细节就不需要知道了。
"""
import abc


class Product:
    '''产品类'''

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print('产品 创建 ----')
        for item in self.parts:
            print(item)


class Builder(abc.ABC):

    @abc.abstractmethod
    def build_part_a(self):
        '''抽象方法A'''

    @abc.abstractmethod
    def build_part_b(self):
        '''抽象方法B'''

    @abc.abstractmethod
    def get_result(self):
        '''抽象方法C'''


class ConcreateBuilder1(Builder):
    '''具体构建者，继承Builder接口，构造和装配各个部件。'''

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add('部件A')

    def build_part_b(self):
        self.product.add('部件B')

    def get_result(self):
        return self.product


class ConcreateBuilder2(Builder):
    '''具体构建者，继承Builder接口，构造和装配各个部件。'''

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add('部件X')

    def build_part_b(self):
        self.product.add('部件Y')

    def get_result(self):
        return self.product


class Director:
    '''指挥者，用来创建产品'''

    def construct(self, builder):
        builder.build_part_a()
        builder.build_part_b()


if __name__ == '__main__':
    director = Director()
    b1 = ConcreateBuilder1()
    b2 = ConcreateBuilder2()

    director.construct(b1)
    p1 = b1.get_result()
    p1.show()

    director.construct(b2)
    p2 = b2.get_result()
    p2.show()
