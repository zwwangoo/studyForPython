import model_v6 as model


@model.entity
class LineItem:
    """
    使用类装饰器在创建类时，设置储存属性的名字::
        >>> raisins = LineItem('Golden raisins', 10, 6.95)
        >>> dir(raisins)[:3]
        ['_NonBlank#description', '_Quantity#price', '_Quantity#weight']
        >>> LineItem.description.storage_name
        '_NonBlank#description'
        >>> raisins.description
        'Golden raisins'
        >>> getattr(raisins, '_NonBlank#description')
        'Golden raisins'
    """
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
