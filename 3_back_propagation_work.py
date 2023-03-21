import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w1 = torch.Tensor([1.0])
w2 = torch.Tensor([1.0])
b = torch.Tensor([1.0])
w1.requires_grad_(True)  
w2.requires_grad_(True)
b.requires_grad_(True)

def forward(x):
    return (x ** 2) * w1 + x * w2 + b

def loss(x,y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

print("predict before training", 4, forward(4).item())


for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)
        l.backward()            #将l的各反向传播梯度保存在变量中，计算图被释放
        print('\tgrad:',x, y, w1.grad.item(), w2.grad.item())    #将w数值标量
        w1.data = w1.data - 0.01 * w1.grad.data    #取data计算，不会建立计算图，.data也是张量
        w2.data = w2.data - 0.01 * w2.grad.data
        w1.grad.zero_()          #权重梯度释放
        w2.grad.zero_() 

    print("progress:", epoch, l.item())

print("predict after training", 4, forward(4).item())