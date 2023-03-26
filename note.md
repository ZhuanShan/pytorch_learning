### **Numpy**
+ ` np.meshgrid` 
```python
W = np.arange(0.0, 4.1, 0.1)
B = np.arange(0.0, 4.1, 0.1)
[w,b] = np.meshgrid(W,B)
```
按照w,b的要求画出网格,适用于绘制三维图形



### **Matplotlib**
+ ``plot``
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



### **Pytorch**

+ ``torch.nn.linear``
```python
m = torch.nn.Linear(20, 30)         #输入维度20，输出维度为30,就是w
input = torch.randn(128, 20)        #x输入为[128,20]
output = m(input)
print(output.size())                #y输出为[128,30]
```
首先创建类对象m，然后通过`m(input)`实际上调用`__call__(input)`，然后`__call__(input)`调用`forward()`函数，最后返回计算结果为：
$$\left[ \begin{matrix}
   128 & 30 \\
  \end{matrix}
  \right] = \left[
 \begin{matrix}
   128 & 20 
  \end{matrix}
  \right] \left[
 \begin{matrix}
   20 & 30 
  \end{matrix}
  \right] $$

参考：(https://blog.csdn.net/dss_dssssd/article/details/82977170)
### **Python**
+ ``__call__, __init__``

```python
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
```
output
```powershell
对象初始化。。。。
我年龄是: 10
forward 函数被调用了
```
这里`a = A(10)`将对象初始化，`init_age`设为10\
`a(2)`是类函数化，将2传入`__call__(self, added_age)`中的`added_age`中\
然后调用`forward()`



## **Pytorch深度学习实践**
### **第五讲Pytorch线性回归**
一个epoch中计算步骤
1. 计算$\hat{y}$
2.   计算loss
3. 计算梯度，进行反向传播
4. 进行更新`.step()`

### **第六讲logistic回归**
分类问题
+ sigmoid函数: 将区间压缩至0-1之间
$$\frac{1}{1+e^{-x}}$$
