'''
几个简单的类，用于研究描述符的覆盖行为。

覆盖型描述符的行为。实现了__set__方法的描述符属于覆盖型描述符，因为虽然描述符
是类属性，但是实现__set__方法的haunted，会覆盖对实例属性的赋值操作::
    >>> obj = Managed()
    >>> obj.over
    -> Overriding.__get__(<Overriding object>, <Managed object>,
        <class Managed>)
    >>> Managed.over
    -> Overriding.__get__(<Overriding object>, None, <class Managed>)
    >>> obj.over = 7
    -> Overriding.__set__(<Overriding object>, <Managed object>, 7)
    >>> obj.over
    -> Overriding.__get__(<Overriding object>, <Managed object>,
        <class Managed>)
    >>> obj.__dict__['over'] = 8
    >>> obj.over
    -> Overriding.__get__(<Overriding object>, <Managed object>,
        <class Managed>)
    >>> vars(obj)
    {'over': 8}

没有__get__方法的覆盖型描述符, 实例属性会遮盖描述符，不过只有读操作如此::
    >>> obj.over_no_get
    <__console__.OverridingNoGet object at 0x7fa9798c8f98>
    >>> Managed.over_no_get
    <__console__.OverridingNoGet object at 0x7fa9798c8f98>
    >>> obj.over_no_get = 7
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get
    <__console__.OverridingNoGet object at 0x7fa9798c8f98>
    >>> obj.__dict__['over_no_get'] = 8
    >>> obj.over_no_get
    8
    >>> obj.over
    -> Overriding.__get__(<Overriding object>, <Managed object>,
        <class Managed>)
    >>> obj.over_no_get = 9
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 9)
    >>> obj.over_no_get
    8

非覆盖型描述符的行为, 如果设置了同名的实例属性，描述符会被遮盖，
导致描述符无法处理那个实例的那个属性::
    >>> obj = Managed()
    >>> obj.non_over
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>,
        <class Managed>)
    >>> obj.non_over = 7
    >>> obj.non_over
    7
    >>> Managed.non_over
    -> NonOverriding.__get__(<NonOverriding object>, None, <class Managed>)
    >>> del obj.non_over
    >>> obj.non_over
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>,
        <class Managed>)

通过类可以覆盖任何描述符, 不管描述符是不是覆盖型，为类属性赋值都能覆盖描述符::
    >>> obj = Managed()
    >>> Managed.over = 1
    >>> Managed.over_no_get = 2
    >>> Managed.non_over = 3
    >>> obj.over, obj.over_no_get, obj.non_over
    (1, 2, 3)
'''


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))
