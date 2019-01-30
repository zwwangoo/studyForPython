"""
职责链模式：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这个对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

    >>> h1 = ConcreteHandler1()
    >>> h2 = ConcreteHandler2()
    >>> h3 = ConcreteHandler3()

    >>> h1.successor = h2  # 设置职责链上家和下家
    >>> h2.successor = h3

    >>> requests = [2, 5, 14, 22, 18, 3, 27, 20]

    >>> for request in requests:
    ...     h1.handle_request(request)
    ConcreteHandler1 处理请求 2
    ConcreteHandler1 处理请求 5
    ConcreteHandler2 处理请求 14
    ConcreteHandler3 处理请求 22
    ConcreteHandler2 处理请求 18
    ConcreteHandler1 处理请求 3
    ConcreteHandler3 处理请求 27
    ConcreteHandler3 处理请求 20

需要注意的地方，一个请求极有可能到了链的末端都得不到处理，或者因为没有正确配置而得不到处理。
"""
import abc


class Handler(abc.ABC):
    def __init__(self):
        self.successor = None

    @abc.abstractmethod
    def handle_request(self, request): pass


class ConcreteHandler1(Handler):

    _name = 'ConcreteHandler1'

    def handle_request(self, request):
        if 0 <= request < 10:
            print(self._name, '处理请求', request)
        elif self.successor:
            self.successor.handle_request(request)


class ConcreteHandler2(Handler):

    _name = 'ConcreteHandler2'

    def handle_request(self, request):
        if 10 <= request < 20:
            print(self._name, '处理请求', request)
        elif self.successor:
            self.successor.handle_request(request)


class ConcreteHandler3(Handler):

    _name = 'ConcreteHandler3'

    def handle_request(self, request):
        if 20 <= request:
            print(self._name, '处理请求', request)
        elif self.successor:
            self.successor.handle_request(request)


if __name__ == '__main__':
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2()
    h3 = ConcreteHandler3()

    h1.successor = h2  # 设置职责链上家和下家
    h2.successor = h3

    requests = [2, 5, 14, 22, 18, 3, 27, 20]

    for request in requests:
        h1.handle_request(request)
