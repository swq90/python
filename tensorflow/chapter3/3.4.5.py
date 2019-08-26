import tensorflow as tf

# 通过numpy工具包生成模拟数据集
from numpy.random import RandomState

# 定义训练数据batch大小
batch_size = 8

# 定义神经网路参数
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

# 在 shape 的一个维度上使用 None 可以方便使用不同的 batch 大小。在训练时需要把数据分 ＃成比较小的 batch， 但是在测试时，可以一次性使用全部的数据。当数据集比较小时这样比较 ＃方便测试，但数据集比较大时，将大量数据放入一个 batch 吁能会导致内存溢出
x = tf.placeholder(tf.float32,shape=(None,2),name='x-input')
y_ = tf.placeholder(tf.float32,shape=(None,1),name='y-input')

# 定义神经网络的传播过程：
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

# 定义损失函数和反向传播算法

