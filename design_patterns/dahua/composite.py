"""
组合模式：将对象组合成树形结构以表示部分整体的层次结构，组合模式使得用户对单个
对象和组合对象的使用具有一致性::
    >>> root = Composite('root')
    >>> root.add(Leaf('Leaf A'))
    >>> root.add(Leaf('Leaf B'))

    >>> comp = Composite('Composite X')
    >>> comp.add(Leaf('Leaf A'))
    >>> comp.add(Leaf('Leaf B'))

    >>> root.add(comp)

    >>> comp2 = Composite('Composite XY')
    >>> comp2.add(Leaf('Leaf A'))
    >>> comp2.add(Leaf('Leaf B'))

    >>> comp.add(comp2)

    >>> root.display(1)
    - root
    -- Leaf A
    -- Leaf B
    -- Composite X
    --- Leaf A
    --- Leaf B
    --- Composite XY
    ---- Leaf A
    ---- Leaf B

组合模式定义了包含基本对象和组合对象的类层次结构，基本对象可以被组合成更复杂的
组合对象，而这个组合对象又可以被组合这样不断地递归下去。
"""
import abc


class Component(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def add(self, c): pass

    @abc.abstractmethod
    def remove(self, c): pass

    @abc.abstractmethod
    def display(self, depth): pass


class Leaf(Component):

    def __init__(self, name):
        super().__init__(name)

    def add(self, c):
        print('cannot add to a leaf')

    def remove(self, c):
        print('cannot remove from a leaf')

    def display(self, depth):
        print('-' * depth, self.name)


class Composite(Component):

    def __init__(self, name):
        self.children = []
        super().__init__(name)

    def add(self, c):
        self.children.append(c)

    def remove(self, c):
        self.children.remove(c)

    def display(self, depth):
        print('-' * depth, self.name)

        for component in self.children:
            component.display(depth + 1)


if __name__ == '__main__':
    root = Composite('root')
    root.add(Leaf('Leaf A'))
    root.add(Leaf('Leaf B'))

    comp = Composite('Composite X')
    comp.add(Leaf('Leaf A'))
    comp.add(Leaf('Leaf B'))

    root.add(comp)

    comp2 = Composite('Composite XY')
    comp2.add(Leaf('Leaf A'))
    comp2.add(Leaf('Leaf B'))

    comp.add(comp2)

    root.display(1)
