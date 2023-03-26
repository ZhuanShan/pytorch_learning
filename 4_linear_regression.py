import torch
# 1.  准备数据集
x_data = torch.tensor([[1.0], [2.0], [3.0]])
y_data = torch.tensor([[2.0], [4.0], [6.0]])

# 2. 设计训练模型
class LinearModel(torch.nn.Module):                 #继承Model类
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)        #构造对象，建立实例torch.nn模块下Linear类 (1,1)表示输入输出维度
#linear内部进行计算w，b，输出y

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred
    
model = LinearModel()

# 3. 构造损失和优化
#损失函数、优化器
criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01) #类进行实例化, model.parameters()自动完成参数的初始化操作

# 4. 训练循环
for epoch in range(100):
    y_pred = model(x_data) 
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())

    loss.backward()                 #反向传播，计算梯度
    optimizer.step()                #更新参数w，b
    optimizer.zero_grad()           #梯度归零

print('w = ', model.linear.weight.item())
print('b = ', model.linear.bias.item())
 
x_test = torch.tensor([[4.0]])
y_test = model(x_test)
print('y_pred = ', y_test.data)
