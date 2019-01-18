import abc


class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print('装扮的{}'.format(self.name))


class Finery(abc.ABC):

    def decorate(self, component):
        self.component = component

    @abc.abstractmethod
    def show(self):
        """抽象类方法"""
        if self.component:
            self.component.show()


class TShirts(Finery):

    def show(self):
        print('大T恤')
        Finery.show(self)


class BigTrouser(Finery):

    def show(self):
        print('垮裤')
        Finery.show(self)


class WearSneakers(Finery):

    def show(self):
        print('破球鞋')
        Finery.show(self)


class WearSuit(Finery):

    def show(self):
        print('西装')
        Finery.show(self)


class WearTie(Finery):

    def show(self):
        print('领带')
        Finery.show(self)


class WearLeatherShoes(Finery):

    def show(self):
        print('皮鞋')
        Finery.show(self)


if __name__ == '__main__':
    xc = Person('小菜')
    print('第一种装扮')
    pqx = WearSneakers()
    kk = BigTrouser()
    dtx = TShirts()

    pqx.decorate(xc)
    kk.decorate(pqx)
    dtx.decorate(kk)
    dtx.show()
