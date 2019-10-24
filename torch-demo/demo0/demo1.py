import os
import torch as t
from torch import optim
from torch import nn
from torch.nn import functional as F

import torchvision as tv
from torchvision import transforms
from torchvision.transforms import ToPILImage

show = ToPILImage()


# 定义网络
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.features = nn.Sequential(
            # 卷积层 '3'表示输入图片为单通道, '6'表示输出通道数，'5'表示卷积核为5*5
            nn.Conv2d(3, 6, 5),
            # 激活
            nn.ReLU(),

            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 16, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        self.classifier = nn.Sequential(
            # 全连接层
            nn.Linear(16 * 5 * 5, 120),

            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10)
        )

    def forward(self, x):
        # 卷积 -> 激活 -> 池化
        x = self.features(x)
        x = x.view(-1, 16 * 5 * 5)
        x = self.classifier(x)
        return x

    def save(self, model_path):
        t.save(self.state_dict(), model_path)


# 定义对数据的预处理
def data():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # 训练集
    trainset = tv.datasets.CIFAR10(
        root='./data/',
        train=True,
        download=True,
        transform=transform)

    trainloader = t.utils.data.DataLoader(
        trainset,
        batch_size=4,
        shuffle=True,
        num_workers=2)

    # 测试集
    testset = tv.datasets.CIFAR10(
        './data/',
        train=False,
        download=True,
        transform=transform)

    testloader = t.utils.data.DataLoader(
        testset,
        batch_size=4,
        shuffle=False,
        num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    data, lable = trainset[100]
    print(classes[lable])
    show((data + 1) / 2).resize((100, 100))
    return trainset, trainloader, testset, testloader, classes


trainset, trainloader, testset, testloader, classes = data()

# 定义损失函数和优化器
net = Net()
criterion = nn.CrossEntropyLoss()  # 交叉熵损失函数

optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)  # 使用随机梯度下降法优化

old_lr = dataiter = iter(trainloader)
images, lables = dataiter.next()
print(' '.join('%ls' % classes[lables[j]] for j in range(4)))
show(tv.utils.make_grid((images + 1) / 2)).resize((400, 100))

if os.path.exists('model.pth'):
    # 加载已有模型
    net.load_state_dict(t.load('model.pth'))
else:
    # 重新训练
    t.set_num_threads(8)
    for epoch in range(4):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, lables = data  # 输入数据

            optimizer.zero_grad()  # 梯度清零

            # forward + backward
            outputs = net(inputs)
            loss = criterion(outputs, lables)
            loss.backward()

            optimizer.step()  # 更新参数

            running_loss += loss.item()
            if i % 2000 == 1999:
                print('[%d, %5d] loss: %.3f'
                      % (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0
    print('Finished Training.')

# 测试
dataiter = iter(testloader)
images, labels = dataiter.next()  # 一个batch返回4张图片
print('实际的label: ', ' '.join(
    '%08s' % classes[labels[j]] for j in range(4)))
show(tv.utils.make_grid(images / 2 - 0.5)).resize((400, 100))
# 计算图片在每个类别上的分数
outputs = net(images)
# 得分最高的那个类
_, predicted = t.max(outputs.data, 1)

print('预测结果: ', ' '.join('%5s'
                         % classes[predicted[j]] for j in range(4)))

correct = 0  # 预测正确的图片数
total = 0  # 总共的图片数


# 由于测试的时候不需要求导，可以暂时关闭autograd，提高速度，节约内存
with t.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = t.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum()

# 保存模型
net.save('model.pth')
print('10000张测试集中的准确率为: %d %%' % (100 * correct / total))
