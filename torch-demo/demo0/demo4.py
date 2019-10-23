import torch as t
from matplotlib import pyplot as plt
import numpy as np

# 设置随机数种子，保证不同电脑输出一致
t.manual_seed(1000)


def get_fake_data(batch_size=8):
    x = t.rand(batch_size, 1) * 5
    y = x * 2 + 3 + t.randn(batch_size, 1)
    return x, y


w = t.rand(1, 1, requires_grad=True)
b = t.zeros(1, 1, requires_grad=True)
# y = w * x + b
losses = np.zeros(500)

lr = 0.005  # 学习率

for ii in range(500):
    x, y = get_fake_data(batch_size=32)

    # forward: 计算loss
    y_pred = x.mm(w) + b.expand_as(y)
    # 总误差 (1 / 2 * (target - output) ** 2).sum()
    loss = (0.5 * (y_pred - y) ** 2).sum()
    losses[ii] = loss.item()

    # 反向传播
    loss.backward()

    # 更新参数
    w.data.sub_(lr * w.grad.data)
    b.data.sub_(lr * b.grad.data)

    # 梯度清零
    w.grad.data.zero_()
    b.grad.data.zero_()

    if ii % 50 == 0:
        # 画图
        x = t.arange(0, 6).view(-1, 1).float()
        y = x.mm(w.data) + b.data.expand_as(x)
        plt.plot(x.numpy(), y.numpy())

        x2, y2 = get_fake_data(batch_size=20)
        plt.scatter(x2.numpy(), y2.numpy())

        plt.xlim(0, 5)
        plt.ylim(0, 13)
        plt.show()
        plt.pause(0.5)
print(w.item(), b.item())

plt.plot(losses)
plt.ylim(5, 50)
plt.show()
