import tensorflow as tf

# 通过numpy工具包生成模拟数据集
from numpy.random import RandomState

# 定义训练数据batch大小
batch_size = 8

# 定义神经网路参数
w1 = tf.Variable(tf.random_normal([2, 3],stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1],stddev=1, seed=1))

# 在 shape 的一个维度上使用 None 可以方便使用不同的 batch 大小。
# 在训练时需要把数据分成比较小的batch，但是在测试时，可以一次性使用全部的数据。
# 当数据集比较小时这样比较方便测试，但数据集比较大时，将大量数据放入一个batch可能会导致内存溢出
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

# 定义神经网络的传播过程：
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播算法
y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(y_*tf.log(tf.clip_by_value(y,1e-10,1.0))+(1-y)*tf.log(tf.clip_by_value(1-y,1e-10,1.0)))
# 定义学习率
#定义反向传播算法优化神经网络中的参数
train_step=  tf.train.AdamOptimizer(0.001).minimize(cross_entropy)


# 通过随机数生成一个模拟数据集


# 定义一个规则给出样本标签，所有x1+x2<1的样例都被认为使正样本（如零件合格）
# 其他样本为负样本，这里0表示负样本，1表示正样本，大部分分类问题的神经网络都用0和1表示方法
Y = [[int(x1+x2<1)]for (x1,x2) in X]

# 创建会话来运行tensorflow


    # 初始化变量

    # 训练之前神经网络参数的值

    # 设定训练轮数

        # 每次选取batch_size个样本进行训练

        # 通过选取的样本训练神经网络并更新参数


            # 每隔一段时间计算所有的数据上的交叉熵并输出u