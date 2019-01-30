"""
命令模式：将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化；对
请求排队或记录请求日志，以及支持可撤销的操作。
    >>> r = Receiver()
    >>> c = ConcreteCommand(r)
    >>> i = Invoker()
    >>> i.command = c
    >>> i.execute_command()
    执行请求！

命令模式的优点：
1 能较容易的设计一个命令队列
2 在需要的情况下，可以较容易的将命令记入日志
3 允许接收请求的一方决定是否要否决请求
4 可以容易的实现对请求的撤销和重做
5 由于加新的具体命令类不影响其他的类，因此增加新的具体命令类很容易
6 命令模式把请求一个操作的对象与知道怎么执行一个操作的对象分割开。

"""
import abc


class Command(abc.ABC):
    """用来声明执行操作的接口"""
    def __init__(self, receiver):
        self.receiver = receiver

    @abc.abstractmethod
    def execute(self): pass


class ConcreteCommand(Command):
    """将一个接收者对象绑定于一个动作，调用接收者相应的操作，以实现Execute"""

    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self):
        self.receiver.action()


class Invoker:
    """要求该命令执行这个请求"""

    def __init__(self):
        self.command = None

    def execute_command(self):
        self.command.execute()


class Receiver:
    """知道如何实施与执行一个与请求相关的操作，任何类都可能作为一个接收者"""
    def action(self):
        print('执行请求！')


if __name__ == '__main__':
    r = Receiver()
    c = ConcreteCommand(r)
    i = Invoker()
    i.command = c
    i.execute_command()
