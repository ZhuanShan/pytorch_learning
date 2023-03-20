import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])
w.requires_grad_(True)         #w需要梯度

def forward(x):
    return x * w    #w是tensor,构建计算图

def loss(x,y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

print("predict before training", 4, forward(4).item())

for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)
        l.backward()            #将l的各反向传播梯度保存在变量中，计算图被释放
        print('\tgrad:',x, y, w.grad.item())    #将w数值标量
        w.data = w.data - 0.01 * w.grad.data    #取data计算，不会建立计算图，.data也是张量
        w.grad.zero_()          #权重梯度释放

    print("progress:", epoch, l.item())

print("predict after training", 4, forward(4).item())

