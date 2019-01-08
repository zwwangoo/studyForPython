class ListItem:
    """
    不用装饰器定义特性的“经典”句法::
        >>> walnuts = LineItem('walnuts', 0, 10.00)
        Traceback (most recent call last):
            ...
        ValueError: value must be > 0
        >>>
    """
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('Value muse be > 0')

    def get_weight(self):
        return self.__weight

    weight = property(get_weight, set_weight)
