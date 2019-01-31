"""
访问者模式：表示一个作用于某对象结构中各元素的操作。它使你可以在不改变各元素的
类的前提下定义于这些元素的新操作::

    >>> o = ObjectStructure()
    >>> o.attach(ConcreteElementA())
    >>> o.attach(ConcreteElementB())

    >>> v1 = ConcreteVisitor1()
    >>> v2 = ConcreteVisitor2()

    >>> o.accept(v1)
    ConcreteElementA被ConcreteVisitor1访问
    ConcreteElementB被ConcreteVisitor1访问

    >>> o.accept(v2)
    ConcreteElementA被ConcreteVisitor2访问
    ConcreteElementB被ConcreteVisitor2访问

访问者模式适用于数据结构相对稳定的系统，它把数据结构作用于结构上的操作之间的耦合
解脱开，使得操作集合可以相对自由地演化。

如果系统有比较稳定的数据结构又有易于变化的算法的话，使用访问者模式是比较合适的
因为该模式使得算法操作的增加变得容易。

缺点：就是使增加新的数据结构变得困难了。
该模式较为复杂。当你真正需要它的时候，才考虑使用它。
"""
import abc


class Visitor(abc.ABC):
    """为该对象结构中ConcreteElement的每个类声明一个Visit操作"""

    @abc.abstractmethod
    def visit_concrete_element_a(self, concrete_element_a): pass

    @abc.abstractmethod
    def visit_concrete_element_b(self, concrete_element_b): pass


class ConcreteVisitor1(Visitor):
    """每个操作实现算法的一部分，而该算法片段乃是对应结构中对象的类"""

    name = 'ConcreteVisitor1'

    def visit_concrete_element_a(self, concrete_element_a):
        print('{}被{}访问'.format(concrete_element_a.name, self.name))

    def visit_concrete_element_b(self, concrete_element_b):
        print('{}被{}访问'.format(concrete_element_b.name, self.name))


class ConcreteVisitor2(Visitor):

    name = 'ConcreteVisitor2'

    def visit_concrete_element_a(self, concrete_element_a):
        print('{}被{}访问'.format(concrete_element_a.name, self.name))

    def visit_concrete_element_b(self, concrete_element_b):
        print('{}被{}访问'.format(concrete_element_b.name, self.name))


class Element(abc.ABC):
    """定义一个Accept操作，它以一个访问者为参数"""

    @abc.abstractmethod
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)


class ConcreteElementA(Element):

    name = 'ConcreteElementA'

    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a():
        pass


class ConcreteElementB(Element):

    name = 'ConcreteElementB'

    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b():
        pass


class ObjectStructure:
    """能枚举它的元素，可以提供一个高层的接口以允许访问者访问它的元素"""

    def __init__(self):

        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def detach(self, element):
        self.elements.remove(element)

    def accept(self, visitor):
        for e in self.elements:
            e.accept(visitor)


if __name__ == '__main__':
    o = ObjectStructure()
    o.attach(ConcreteElementA())
    o.attach(ConcreteElementB())

    v1 = ConcreteVisitor1()
    v2 = ConcreteVisitor2()

    o.accept(v1)
    o.accept(v2)
