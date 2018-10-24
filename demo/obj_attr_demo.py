"""
与实例属性访问相关的方法
"""
class A:
    a = 1234


class B(A):
    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        """
        当整个搜索路径都找不到目标属性时触发
        """
        print(f'get: {name}')
        return self.__dict__.get(name)

    def __setattr__(self, name, value):
        """
        拦截对任何属性的赋值操作
        """
        print(f'set: {name} = {value}')
        self.__dict__[name] = value

    def __delattr__(self, name):
        """
        拦截对任何属性的删除操作
        """
        print(f'del: {name}')
        self.__dict__.pop(name, None)


if __name__ == '__main__':
    o = B(1)
    print(o.a, '搜索路径里能找到的成员，不会触发__getattr__')
    print(o.xxx, '找不到， 才会触发')
    o.x = 100
    del o.x
