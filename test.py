# import numpy as np
# import matplotlib.pyplot as plt
# import random

# x_data = [1.0, 2.0, 3.0]
# y_data = [2.0, 4.0, 6.0]

# sample_list = [i for i in range(len(x_data))]
# sample_list = random.sample(sample_list, 2)
# sample_x = [x_data[i] for i in sample_list]
# sample_y = [y_data[i] for i in sample_list]


# print(sample_x)

import torch

# m = torch.nn.Linear(20, 30)         #输入维度60，输出40
# input = torch.randn(128, 20)         #输入为
# output = m(input)
# print(output.size())

class A():
    def __init__(self, init_age):
        super().__init__()
        print('我年龄是:',init_age)
        self.age = init_age
 
    def __call__(self, added_age):
        res = self.forward(added_age)
        return res
 
    def forward(self, input_):
        print('forward 函数被调用了')
        
        return input_ + self.age
print('对象初始化。。。。')
a = A(10)

input_param = a(2)
 

 
 