"""
适配器模式：将一个类的接口转换成客户希望的另外一个接口。使得原本由于接口不兼容
而不能一起工作的那些类可以一起工作::
    >>> target = Adapter()
    >>> target.request()
    特殊请求
"""
import abc


class Target(abc.ABC):
    """这是客户期待的接口，目标可以是具体的或抽象的类，也可以是接口"""

    @abc.abstractmethod
    def request(self):
        print('普通请求')


class Adaptee:
    """需要适配的类"""
    def specific_request(self):
        print('特殊请求')


class Adapter(Target):
    """通过内部包装一个Adaptee对象，把源接口转换成目标接口"""

    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        return self.adaptee.specific_request()


if __name__ == "__main__":
    target = Adapter()
    target.request()
