class LineItem:
    '''
    使用装饰器定义特性::
        >>> walnuts = LineItem('walnuts', 0, 10.00)
        Traceback (most recent call last):
            ...
        ValueError: value must be > 0
        >>>
    '''
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
