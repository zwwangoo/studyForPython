"""
工厂方法模式，定义一个用于创建对象的接口，让子类决定实例化哪个类。
工厂方法使一个类的实例化延迟到其子类。
代码示例：学习雷锋好榜样，继承雷锋精神的大学生和社区的构建::
    >>> factory = UndergraduateFactory()
    >>> student = factory.create_leifeng()
    >>> student.buyrice()
    买米
    >>> student.sweep()
    扫地
    >>> student.wash()
    洗衣

工厂方法把简单工厂的内部逻辑判断移到了客户端代码来进行。
"""
import abc


class LeiFeng:

    def sweep(self):
        print('扫地')

    def wash(self):
        print('洗衣')

    def buyrice(self):
        print('买米')


class IFactory(abc.ABC):

    @abc.abstractmethod
    def create_leifeng(self):
        """工厂接口"""


class Undergraduate(LeiFeng):
    """继承雷锋精神的大学生类"""


class Volunteer(LeiFeng):
    """继承雷锋精神的社区志愿者类"""


class UndergraduateFactory(IFactory):
    """大学生工厂"""

    def create_leifeng(self):
        return Undergraduate()


class VolunteerFactory(IFactory):
    """社区志愿者工厂"""

    def create_leifeng(self):
        return Volunteer()


if __name__ == '__main__':
    factory = UndergraduateFactory()  # 要换成 “社区志愿者”，修改这里就可以了
    student = factory.create_leifeng()

    student.buyrice()
    student.sweep()
    student.wash()
