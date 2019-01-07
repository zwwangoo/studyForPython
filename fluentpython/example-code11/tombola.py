import abc


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中，添加对象
        """
        pass

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
        如果实例为空，这个方法应该抛出LookupError
        """
        pass

    def loaded(self):
        """至少存在一个元素，返回True, 否则返回False
        """
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序的元组，由当前元素构成
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
