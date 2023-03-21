import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_data = [1.0, 2.0, 3.0]
y_data = [1.5, 4.0, 6.5]

def forward(x):
    return x*w + b

def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

W = np.arange(0.0, 4.1, 0.1)
B = np.arange(-2.0, 2.1, 0.1)
[w,b] = np.meshgrid(W,B)

l_sum = 0
mse_list = []
for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val)
    loss_val = loss(x_val, y_val)
    l_sum += loss_val
    print('\t', x_val, y_val, y_pred_val, loss_val)
mse_list.append(l_sum/3)
print('MSE:',l_sum / 3)

fig = plt.figure(figsize=(7,5), dpi=100)          # 创建一个画布
ax = Axes3D(fig)            #将fig变为3D
ax.set_xlabel("w")          #设置x轴名字
ax.set_ylabel("b")
ax.set_zlim(0, 40)          #设置z轴区间
ax.set_zlabel("loss")
ax.plot_surface(w, b, l_sum /3)        #设置x，y， z
plt.show()