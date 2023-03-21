import torch

x_data = torch.tensor([[1.0], [2.0], [3.0]])
y_data = torch.tensor([[2.0], [4.0], [6.0]])

class LinearModel(torch.nn.Module):          #继承Model类
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linerar(1, 1)        #构造对象，torch.nn模块下Linear类 (1,1)表示输入输出维度

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred
    
model = LinearModel()