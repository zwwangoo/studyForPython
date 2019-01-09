'''
特性工厂函数的实现::
    >>> coconuts = LineItem('Brzaillian coconut', 20, 17.95)
    >>> coconuts.weight, coconuts.price
    (20, 17.95)
    >>> getattr(coconuts, '_Quantity:0'), getattr(coconuts, '_Quantity:1')
    (20, 17.95)
'''


def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity()
    price = quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
