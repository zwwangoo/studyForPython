import model_v7 as model


class LineItem(model.Entity):
    """
    定制描述符的元类，有了元类的支持，集成model.Entity类即可::
        >>> raisins = LineItem('Golden raisins', 10, 6.95)
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
