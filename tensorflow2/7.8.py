import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def himmelblau(x):
    # himmelblau 函数实现
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


# 通过 np.meshgrid 函数(TensorFlow 中也有 meshgrid 函数)生成二维平面网格点坐标：
x = np.arange(-6, 6, 0.1)
y = np.arange(-6, 6, 0.1)
print('x,y range:', x.shape, y.shape)
# 生成 x-y 平面采样网格点，方便可视化
X, Y = np.meshgrid(x, y)
print('X,Y maps:', X.shape, Y.shape)
Z = himmelblau([X, Y])  # 计算网格点上的函数值
# 并利用 Matplotlib 库可视化 Himmelblau 函数，如图 7.11 所示。
# 绘制 himmelblau 函数曲面
fig = plt.figure('himmelblau')
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z)
ax.view_init(60, -30)
ax.set_xlabel('x')
ax.set_ylabel('y')
# plt.show()
x = tf.constant([4., 0.])  # 初始化参数

for step in range(200):  # 循环优化 200 次
    with tf.GradientTape() as tape:  # 梯度跟踪
        tape.watch([x])  # 加入梯度跟踪列表
        y = himmelblau(x)  # 前向传播
    # 反向传播
    grads = tape.gradient(y, [x])[0]
    # 更新参数,0.01 为学习率
    x -= 0.01 * grads
    # 打印优化的极小值
    if step % 20 == 19:
        print('step {}: x = {}, f(x) = {}'
              .format(step, x.numpy(), y.numpy()))
print()
