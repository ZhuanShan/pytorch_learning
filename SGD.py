#随机选取部分样本，随机梯度下降


import numpy as np
import matplotlib.pyplot as plt
import random

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0

def forward(x):
    return x * w

def loss(xs, ys):                       #计算mse
    loss = 0
    for x, y in zip(xs, ys):
        y_pred = forward(x)
        loss += (y_pred - y) ** 2
    print(len(xs))
    return loss / len(xs)

def gradient(xs, ys):                   #求梯度
    grad = 0
    for x, y in zip(xs, ys):
        grad += 2 * x * (x * w - y)
    return grad


def rand(num):                                  #随机选取num个样本
    sample_list = [i for i in range(len(x_data))]
    sample_list = random.sample(sample_list, num)
    sample_x = [x_data[i] for i in sample_list]
    sample_y = [y_data[i] for i in sample_list]
    return sample_x, sample_y 
    



epoch_list = []
loss_list = []

print('predict (before training)', 4, forward(4))
for epoch in range(100):                            #迭代
    (sample_x,sample_y) = rand(2)
    print(sample_x)
    loss_val = loss(sample_x, sample_y)
    grad_val = gradient(sample_x, sample_y)
    w = w - 0.01 * grad_val
    print('Epoch:', epoch, 'w=', w, 'loss=', loss_val)
    epoch_list.append(epoch)
    loss_list.append(loss_val)

print('predict(after training)', 4, forward(4))


plt.plot(epoch_list, loss_list)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()
