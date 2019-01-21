"""
原型模式：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
其实就是从一个对象再创建另外一个可定制的对象，并且不需要知道任何创建的细节::

    >>> a = Resume('大鸟')
    >>> a.set_personal_info('男', '29')
    >>> a.set_work_experience('1998-2000', 'xx公司')

    >>> b = a.clone()
    >>> b.set_work_experience('2000-2006', 'xx企业')

    >>> c = a.clone()
    >>> c.set_personal_info('男', '24')

    >>> a.display()
    大鸟 男 29
    工作经历: 1998-2000 xx公司
    >>> b.display()
    大鸟 男 29
    工作经历: 2000-2006 xx企业
    >>> c.display()
    大鸟 男 24
    工作经历: 1998-2000 xx公司

一般在初始化的信息不发生变化的情况下，克隆是最好的办法，它既隐藏了对象的创建
细节，又对性能是大大的提升。
"""
import abc
import copy


class Prototype(abc.ABC):

    @abc.abstractmethod
    def clone(self):
        """"""


class Resume(Prototype):

    def __init__(self, name):
        self.name = name

    def set_personal_info(self, sex, age):
        self.sex = sex
        self.age = age

    def set_work_experience(self, time_area, company):
        self.time_area = time_area
        self.company = company

    def display(self):
        print('{} {} {}'.format(self.name, self.sex, self.age))
        print('工作经历: {} {}'.format(self.time_area, self.company))

    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    a = Resume('大鸟')
    a.set_personal_info('男', '29')
    a.set_work_experience('1998-2000', 'xx公司')

    b = a.clone()
    b.set_work_experience('2000-2006', 'xx企业')

    c = a.clone()
    c.set_personal_info('男', '24')

    a.display()
    b.display()
    c.display()
