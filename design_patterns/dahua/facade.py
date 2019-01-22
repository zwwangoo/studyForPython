"""
外观模式：为子系统中的一组接口提供一个一致的界面，此模式定义了一个高层接口，
这个接口使得这一子系统更加容易使用::
    >>> facade = Facade()
    >>> facade.method_a()
    --- 方法组A() ---
    子系统方法一
    子系统方法二
    子系统方法四
    >>> facade.method_b()
    --- 方法组B() ---
    子系统方法二
    子系统方法三

外观模式完美的体现了依赖倒转原则和迪米特法则的思想，是常用的模式之一。
经典的三层架构，就需要考虑在层与层之间建立外观Facade。
"""


class SubSystemOne:

    def methode_one(self):
        print('子系统方法一')


class SubSystemTwo:

    def methode_two(self):
        print('子系统方法二')


class SubSystemThree:

    def methode_three(self):
        print('子系统方法三')


class SubSystemFour:

    def methode_four(self):
        print('子系统方法四')


class Facade:
    """外观类"""

    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def method_a(self):
        print('--- 方法组A() ---')
        self.one.methode_one()
        self.two.methode_two()
        self.four.methode_four()

    def method_b(self):
        print('--- 方法组B() ---')
        self.two.methode_two()
        self.three.methode_three()


if __name__ == '__main__':
    facade = Facade()
    facade.method_a()
    facade.method_b()
