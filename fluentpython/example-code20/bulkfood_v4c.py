import model_v4c as model


class LineItem:
    # 这里的方式非常像模型定义，Django中模型的字段就是描述符
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
