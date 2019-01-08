import keyword
from collections import abc


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
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):  # 关键字键名进行处理
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            if not self.__data.get(name):
                raise AttributeError
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
