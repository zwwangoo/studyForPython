from random import randrange

from tombola import Tombola


@Tombola.register  # 把TomboList 注册为Tombola的虚拟子类
class TomboList(list):  # 拓展list

    def pick(self):
        if self:  # TomboList 从list中继承　__bool__方法，列表不为空时，返回True
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
