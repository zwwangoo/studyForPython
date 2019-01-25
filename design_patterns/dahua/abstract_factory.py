"""
抽象工厂方法：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体
的类::

    >>> user = User()
    >>> dept = Department()
    >>> factory = SqlserverFactory()
    >>> iu = factory.create_user()
    >>> iu.insert(user)
    在sql server 中给User表增加一条记录
    >>> iu.get_user(1)
    在sql server 中根据ID得到User表一条记录

    >>> factory = AccessFactory()
    >>> id = factory.create_department()
    >>> id.insert(dept)
    在Access中给Department表增加一条记录
    >>> id.get_dept(1)
    在Access中根据ID得到Department表一条记录
    >>> iu = factory.create_user()
    >>> iu.insert(user)
    在Access中给User表增加一条记录
    >>> iu.get_user(1)
    在Access中根据Id得到User表一条记录


抽象工厂模式的优点：
1、易于交换产品系列，由于具体工厂类，在一个应用中只需要在初始化的时候出现一次，
这就使得改变一个应用的具体工厂变得非常容易，它只需要改变具体工厂即可使用不 同
的产品配置。
2、让具体的创建实例过程和客户端分离，客户端是通过它们的抽象接口操作实例，产品
的具体类名也被具体工厂的实现分离，不会出现在客户代码中。

缺点：
新增或修改时，可能需要大量的改动。
"""
import abc


class User:

    id = None
    name = None


class Department:
    id = None
    dept_name = None


class IUser(abc.ABC):

    @abc.abstractmethod
    def insert(self, user):
        pass

    @abc.abstractmethod
    def get_user(self, id):
        pass


class IDepartment(abc.ABC):

    @abc.abstractmethod
    def insert(self, dept):
        pass

    @abc.abstractmethod
    def get_dept(self, id):
        pass


class IFactory(abc.ABC):

    @abc.abstractmethod
    def create_user(self):
        pass

    @abc.abstractmethod
    def create_department(self):
        pass


class SqlserverUser(IUser):

    def insert(self, user):
        print('在sql server 中给User表增加一条记录')

    def get_user(self, id):
        print('在sql server 中根据ID得到User表一条记录')
        return None


class SqlserverDepartment(IDepartment):

    def insert(self, dept):
        print('在sql server 中给Department表中增加一条记录')

    def get_dept(self, id):
        print('在sql server 中根据ID得到Department表一条记录')


class AccessUser(IUser):

    def insert(self, user):
        print('在Access中给User表增加一条记录')

    def get_user(self, id):
        print('在Access中根据Id得到User表一条记录')


class AccessDepartment(IDepartment):

    def insert(self, department):
        print('在Access中给Department表增加一条记录')

    def get_dept(self, id):
        print('在Access中根据ID得到Department表一条记录')


class SqlserverFactory(IFactory):

    def create_user(self):
        return SqlserverUser()

    def create_department(self):
        return SqlserverDepartment()


class AccessFactory(IFactory):

    def create_user(self):
        return AccessUser()

    def create_department(self):
        return AccessDepartment()


if __name__ == '__main__':
    user = User()
    dept = Department()
    # factory = SqlserverFactory()
    factory = AccessFactory()

    iu = factory.create_user()
    iu.insert(user)
    iu.get_user(1)

    id = factory.create_department()
    id.insert(dept)
    id.get_dept(1)
