"""
备忘录模式：在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存
这个状态。这样就可以将该对象恢复到原先保存的状态::
    >>> o = Originator()
    >>> o.state = 'ON'  # 初始状态
    >>> o.show()
    state= ON

    >>> caretaker = Caretaker()
    >>> caretaker.memento = o.create_memento()

    >>> o.state = 'OFF'  # 改变状态
    >>> o.show()
    state= OFF

    >>> o.set_memento(caretaker.memento)  # 恢复
    >>> o.show()
    state= ON

缺点：当需要备忘的对象状态数据很大很多时，那么在资源消耗上，备忘录对象会非常消耗资源。
"""


class Originator:

    def __init__(self):
        self.state = None

    def create_memento(self):
        """创建备忘录，将当前需要保存的信息导入并实例化一个备忘录对象。"""
        return Memento(self.state)

    def set_memento(self, memento):
        """恢复备忘录"""
        self.state = memento.state

    def show(self):
        print('state=', self.state)


class Memento:
    """备忘录"""

    def __init__(self, state):
        self.state = state


class Caretaker:
    """管理者，负责保存好备忘录，不能对备忘录的内容进行操作或检查。"""

    def __init__(self):
        self.memento = None


if __name__ == '__main__':
    o = Originator()
    o.state = 'ON'  # 初始状态
    o.show()

    caretaker = Caretaker()
    caretaker.memento = o.create_memento()

    o.state = 'OFF'  # 改变状态
    o.show()

    o.set_memento(caretaker.memento)  # 恢复
    o.show()
