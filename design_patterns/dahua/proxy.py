"""
代理模式：为其他对象提供一种代理以控制对这个对象的访问。
代码示例：A追求C，委托B送礼物给C。需求的重点是A和C不能直接接触::
    >>> jiaojiao = SchoolGirl()
    >>> jiaojiao.name = '李娇娇'
"""

import abc


class SchoolGirl:

    def __init__(self, name):
        self.name = name


class IGiveGift(abc.ABC):
    """代理接口"""

    @abc.abstractmethod
    def give_dolls(self):
        """送洋娃娃"""

    @abc.abstractmethod
    def give_flowers(self):
        """送鲜花"""

    @abc.abstractmethod
    def give_chocolate(self):
        """送巧克力"""


class Pursuit(IGiveGift):
    """追求者"""

    def __init__(self, mm):
        self.mm = mm

    def give_dolls(self):
        print(self.mm.name, '送你洋娃娃')

    def give_flowers(self):
        print(self.mm.name, '送你鲜花')

    def give_chocolate(self):
        print(self.mm.name, '送你巧克力')


class Proxy(IGiveGift):
    """代理者"""

    def __init__(self, mm):
        self.gg = Pursuit(mm)

    def give_dolls(self):
        self.gg.give_dolls()

    def give_flowers(self):
        self.gg.give_flowers()

    def give_chocolate(self):
        self.gg.give_chocolate()


if __name__ == '__main__':
    c = SchoolGirl('c')

    a = Pursuit(c)
    a.give_dolls()
    a.give_flowers()
    a.give_chocolate()
