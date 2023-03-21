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

m = torch.nn.Linear(20, 30)         #输入维度60，输出40
input = torch.randn(128, 20)         #输入为
output = m(input)
print(output.size())
