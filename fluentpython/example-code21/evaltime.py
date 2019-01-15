'''
在Python控制台中导入evaltime模块::
    <10> evalsupport module start
    <400> MetaAleph body
    <700> evalsupport module end
    <1> evaltime module start
    <2> ClassOne body
    <6> ClassTwo body
    <7> ClassThree body
    <200> deco_alpha
    <9> ClassFour body
    <14> evalsupport module end

在shell中运行evaltime.py
    $ python evaltime.py
    <10> evalsupport module start
    <400> MetaAleph body
    <700> evalsupport module end
    <1> evaltime module start
    <2> ClassOne body
    <6> ClassTwo body
    <7> ClassThree body
    <200> deco_alpha
    <9> ClassFour body
    <11> ClassOne tests ------------------------------
    <3> ClassOne.__init__
    <5> ClassOne.method_x
    <12> ClassThree tests ------------------------------
    <300> deco_alpha:inner_1
    <13> ClassFour tests ------------------------------
    <10> ClassFour.method_y
    <14> evalsupport module end
    <4> ClassOne.__del__
'''

from evalsupport import deco_alpha

print('<1> evaltime module start')


class ClassOne():
    print('<2> ClassOne body')

    def __init__(self):
        print('<3> ClassOne.__init__')

    def __del__(self):
        print('<4> ClassOne.__del__')

    def method_x(self):
        print('<5> ClassOne.method_x')

    class ClassTwo(object):
        print('<6> ClassTwo body')


@deco_alpha
class ClassThree():
    print('<7> ClassThree body')

    def method_y(self):
        print('<8> ClassThree body')


class ClassFour(ClassThree):
    print('<9> ClassFour body')

    def method_y(self):
        print('<10> ClassFour.method_y')


if __name__ == '__main__':
    print('<11> ClassOne tests', 30 * '-')
    one = ClassOne()
    one.method_x()
    print('<12> ClassThree tests', 30 * '-')
    three = ClassThree()
    three.method_y()
    print('<13> ClassFour tests', 30 * '-')
    four = ClassFour()
    four.method_y()


print('<14> evalsupport module end')
