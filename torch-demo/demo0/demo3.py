import torch as t
from torch.autograd import Function


class MultplyAdd(Function):

    @staticmethod
    def forward(ctx, w, x, b):
        ctx.save_for_backward(w, x)
        output = w * x + b
        return output

    @staticmethod
    def backward(ctx, grad_output):
        w, x = ctx.saved_tensors
        grad_w = grad_output * x
        grad_x = grad_output * w
        grad_b = grad_output * 1
        return grad_w, grad_x, grad_b


x = t.ones(1)
w = t.rand(1, requires_grad=True)
b = t.rand(1, requires_grad=True)

# 开始前向传播
z = MultplyAdd.apply(w, x, b)
# 开始后向传播
z.backward()
print(x.grad, w.grad, b.grad)


def f(x):
    y = x ** 2 * t.exp(x)
    return y


def gradf(x):
    dx = 2 * x * t.exp(x) + x ** 2 * t.exp(x)
    return dx


x = t.randn(3, 4, requires_grad=True)
y = f(x)
y.backward(t.ones(y.size()))
print(x.grad)
print(gradf(x))
