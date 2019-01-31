"""
解释器模式：给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器
使用该表示来解释语言中的句子::
    >>> context = Context()
    >>> ll = []
    >>> ll.append(TerminalExpression())
    >>> ll.append(TerminalExpression())
    >>> ll.append(NonterminalExpression())
    >>> ll.append(TerminalExpression())

    >>> for exp in ll:
    ...     exp.interpret(context)
    终端解释器
    终端解释器
    非终端解释器
    终端解释器

比如，在字符串搜索匹配的字符或判断一个字符串是否符合我们规定的格式，我们会用到
的正则表达式技术，就是该模式的很好应用。

优点：容易的改变和扩展文法，因为该模式使用类来表示文法规则，你可使用继承来改变
或扩展该方法。也比较容易实现文法，因为定义抽象语法树中各个节点的类的实现大体类
似，这些类都易于直接编写。

缺点：该模式为文法中的每一条规则至少定义了一个类，因此包含许多规则的文法就很难
管理和维护。建议当文法非常复杂时，使用其他的技术如语法分析程序或编译器生成器来
处理。
"""
import abc


class AbstractExpression(abc.ABC):

    @abc.abstractmethod
    def interpret(self, context): pass


class TerminalExpression(AbstractExpression):

    def interpret(self, context):
        print('终端解释器')


class NonterminalExpression(AbstractExpression):

    def interpret(self, context):
        print('非终端解释器')


class Context:

    def __init__(self):
        self.input = ''
        self.output = ''


if __name__ == '__main__':

    context = Context()
    ll = []
    ll.append(TerminalExpression())
    ll.append(TerminalExpression())
    ll.append(NonterminalExpression())
    ll.append(TerminalExpression())

    for exp in ll:
        exp.interpret(context)
