"""
2019-01-16
简单工厂模式:::
    >>> oper = OperationFactory.create_operate('+')
    >>> oper.number1 = 12
    >>> oper.number2 = 13
    >>> oper.get_result()
    25
    >>> oper = OperationFactory.create_operate('/')
    >>> oper.number1 = 12
    >>> oper.number2 = 0
    >>> oper.get_result()
    Traceback (most recent call last):
        ...
    ValueError: 除数不能为0
"""
import abc


class Operation(abc.ABC):
    """运算类，抽象类"""
    def __init__(self):
        self._number1 = None
        self._number2 = None

    @property
    def number1(self):
        return self._number1

    @number1.setter
    def number1(self, value):
        self._number1 = value

    @property
    def number2(self):
        return self._number2

    @number2.setter
    def number2(self, value):
        self._number2 = value

    @abc.abstractmethod
    def get_result(self):
        """返回计算结果, 子类需要实现该方法"""


class OperationAdd(Operation):
    """加法类"""
    def get_result(self):
        return self.number1 + self.number2


class OperationSub(Operation):
    """减法类"""
    def get_result(self):
        return self.number1 - self.number2


class OperationMul(Operation):
    """乘法类"""
    def get_result(self):
        return self.number1 * self.number2


class OperationDiv(Operation):
    """除法类"""
    def get_result(self):
        if self.number2 == 0:
            raise ValueError('除数不能为0')
        return self.number1 / self.number2


class OperationFactory:
    """简单运算工厂类"""
    @classmethod
    def create_operate(cls, operate):
        oper = None
        if operate == '+':
            oper = OperationAdd()
        elif operate == '-':
            oper = OperationSub()
        elif operate == '*':
            oper = OperationMul()
        elif operate == '/':
            oper = OperationDiv()
        return oper
