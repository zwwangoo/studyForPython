from collections import abc
from keyword import iskeyword


class FrozenJSON:
    '''
    一个只读接口，使用属性表示法访问JSON类对象::
        >>> f = FrozenJSON({'name': 12, 'class': '25'})
        >>> f
        <explore1.FrozenJSON object at 0x7efce880c6a0>
        >>> f.keys()
        dict_keys(['name', 'class_'])
        >>>
    '''

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):  # 关键字键名进行处理
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self._data[name])
