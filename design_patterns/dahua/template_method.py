"""
模板方法模式：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中，模板方法是的子类可以
不改变一个算法的结构即可重新定义该算法的特定步骤::
    >>> a = ConcreteClassA()
    >>> a.template_method()
    具体类A方法1实现
    具体类A方法2实现
    >>> b = ConcreteClassB()
    >>> b.template_method()
    具体类B方法1实现
    具体类B方法2实现
"""
import abc


class AbstractClass(abc.ABC):

    def template_method(self):
        """模板方法，给出逻辑的骨架，而逻辑的组成是一些相应的抽象操作，它们都推迟到子类实现。"""
        self.primitive_operation1()
        self.primitive_operation2()

    @abc.abstractmethod
    def primitive_operation1(self):
        """抽象行为1放到子类去实现"""

    @abc.abstractmethod
    def primitive_operation2(self):
        """抽象行为2放到子类去实现"""


class ConcreteClassA(AbstractClass):

    def primitive_operation1(slef):
        print('具体类A方法1实现')

    def primitive_operation2(slef):
        print('具体类A方法2实现')


class ConcreteClassB(AbstractClass):

    def primitive_operation1(slef):
        print('具体类B方法1实现')

    def primitive_operation2(slef):
        print('具体类B方法2实现')


if __name__ == '__main__':
    c = ConcreteClassA()
    c.template_method()

    d = ConcreteClassB()
    d.template_method()
