### Numpy
` np.meshgrid` 使用
```python
W = np.arange(0.0, 4.1, 0.1)
B = np.arange(0.0, 4.1, 0.1)
[w,b] = np.meshgrid(W,B)
```
按照w,b的要求画出网格



### Matplotlib

```python
fig = plt.figure(figsize=(10,10), dpi=300) # 创建一个画布
ax = Axes3D(fig)            #将fig变为3D
ax.set_xlabel("w")          #设置x轴名字
ax.set_ylabel("b")
ax.set_zlim(0, 40)          #设置z轴区间
ax.set_zlabel("loss")
ax.plot_surface(w, b, l_sum /3)        #设置x，y， z
plt.show()
```