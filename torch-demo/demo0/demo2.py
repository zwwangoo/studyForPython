import torch as t
from matplotlib import pyplot as plt
device = t.device('cpu')

t.manual_seed(1000)


def get_fake_data(batch_size=8):
    x = t.rand(batch_size, 1, device=device) * 5
    y = x * 2 + 3 + t.randn(batch_size, 1, device=device)
    return x, y


# x, y = get_fake_data(batch_size=16)
# plt.scatter(x.squeeze().cpu().numpy(), y.squeeze().cpu().numpy())

w = t.rand(1, 1).to(device)
b = t.zeros(1, 1).to(device)
lr = 0.02

for ii in range(500):
    x, y = get_fake_data(batch_size=4)

    y_pred = x.mm(w) + b.expand_as(y)
    loss = 0.5 * (y_pred - y) ** 2
    loss = loss.mean()
    dloss = 1
    dy_pred = dloss * (y_pred - y)

    dw = x.t().mm(dy_pred)
    db = dy_pred.sum()

    w.sub_(lr * dw)
    b.sub_(lr * db)
    if ii % 50 == 0:
        x = t.arange(0, 6).view(-1, 1).float()
        y = x.mm(w) + b.expand_as(x)
        plt.plot(x.cpu().numpy(), y.cpu().numpy())

        x2, y2 = get_fake_data(batch_size=32)
        plt.scatter(x2.numpy(), y2.numpy())

        plt.xlim(0, 5)
        plt.ylim(0, 13)
        plt.show()
        plt.pause(0.5)
print('w: ', w.item(), 'b: ', b.item())
