import torch as t
from torch import nn


class Linear(nn.Module):

    def __init__(self, in_features, out_features):
        super(Linear, self).__init__()
        self.w = nn.Parameter(t.randn(in_features, out_features))
        self.b = nn.Parameter(t.randn(out_features))

    def forward(self, x):
        x = x.mm(self.w)
        return x + self.b.expand_as(x)


layer = Linear(4, 3)
input = t.randn(2, 4)
output = layer(input)
print(output)

for name, parameter in layer.named_parameters():
    print(name, parameter)
