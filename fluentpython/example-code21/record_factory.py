def record_factory(cls_name, field_names):
    """
    一个简单的类工厂::
        >>> Dog = record_factory('Dog', 'name weight owner')
        >>> rex = Dog('Rex', 30, 'Bob')
        >>> rex
        Dog(name='Rex', weight=30, owner='Bob')
        >>> name, weight, _ = rex
        >>> name, weight
        ('Rex', 30)
        >>> rex.weight = 32
        >>> rex
        Dog(name='Rex', weight=32, owner='Bob')
        >>> Dog.__mro__  # 新建的类继承与object，与我们的工厂函数没有关系。
        (<class '__console__.Dog'>, <class 'object'>)
        >>>
    """
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i
                           in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(
        __slots__=field_names,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__,
    )
    return type(cls_name, (object,), cls_attrs)
