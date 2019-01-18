"""
2019-01-16
策略模式::
    >>> csuper = CashContext('正常收费')
    >>> csuper.get_result(20)
    20.0
    >>> csuper = CashContext('满300返100')
    >>> csuper.get_result(300)
    200.0
    >>> csuper.get_result(200)
    200.0
    >>> csuper = CashContext('打八折')
    >>> csuper.get_result(300)
    240.0
"""
import abc


class CashSuper(abc.ABC):

    @abc.abstractmethod
    def accept_cash(self, money):
        """现金收取超类的抽象方法，收取现金参数为原价，返回为当前价"""


class CashNormal(CashSuper):
    """原价收费"""

    def accept_cash(self, money):
        return float(money)


class CashRebate(CashSuper):
    """打折收费"""

    def __init__(self, money_rebate):
        self.money_rebate = float(money_rebate)

    def accept_cash(self, money):
        return money * self.money_rebate


class CashReturn(CashSuper):
    """返利收费"""

    def __init__(self, money_condition, money_return):
        self.money_condition = float(money_condition)
        self.money_return = float(money_return)

    def accept_cash(self, money):
        money = float(money)
        result = money
        if money >= self.money_condition:
            result = money - money / self.money_condition * self.money_return
        return result


class CashContext:

    def __init__(self, type):
        if type == '正常收费':
            self.cs = CashNormal()
        elif type == '满300返100':
            self.cs = CashReturn('300', '100')
        elif type == "打八折":
            self.cs = CashRebate('0.8')
        else:
            raise ValueError('输入错误')

    def get_result(self, money):
        return self.cs.accept_cash(money)
