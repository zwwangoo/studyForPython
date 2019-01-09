'''
使用描述符管理属性::
    >>> truffle = LineItem('White truffle', 100, 0)
    Traceback (most recent call last):
        ...
    ValueError: value must be > 0
'''


class Quantity:

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        '''
        self: 描述符实例
        instance: 托管的实例
        '''
        if value > 0:
            # 这里必须使用__dict__属性，如果使用内置的setattr函数，
            # 会再次触发__set__方法，导致无限递归
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:

    weight = Quantity('weight')  # Quantity实例是LineItem类的类属性
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
