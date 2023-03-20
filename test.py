import numpy as np
import matplotlib.pyplot as plt
import random

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

sample_list = [i for i in range(len(x_data))]
sample_list = random.sample(sample_list, 2)
sample_x = [x_data[i] for i in sample_list]
sample_y = [y_data[i] for i in sample_list]


print(sample_x)