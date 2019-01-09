'''
为了避免在描述符声明语句中重复输入属性名，将每个Quantity
实例的storage_name属性生成一个对无二的字符串::
    >>> coconuts = LineItem('Brzaillian coconut', 20, 17.95)
    >>> coconuts.weight, coconuts.price
    (20, 17.95)
    >>> getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1')
    (20, 17.95)
'''


class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        # 托管的属性和存储属性的名称不同，所以这里可以使用getattr
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
