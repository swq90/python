import tensorflow as tf

# 通过numpy工具包生成模拟数据集
import numpy.random

# 定义训练数据batch大小
batch_size = 8

# 定义神经网路参数
# tf.random_normal，seed参数设置随机种子，可以保证每次运行得到的结果一致

w1 = tf.Variable(tf.random.normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random.normal([3, 1], stddev=1, seed=1))

# 在 shape 的一个维度上使用 None 可以方便使用不同的 batch 大小。
# 在训练时需要把数据分成比较小的batch，但是在测试时，可以一次性使用全部的数据。
# 当数据集比较小时这样比较方便测试，但数据集比较大时，将大量数据放入一个batch可能会导致内存溢出
# tf.placeholder
x = tf.compat.v1.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.compat.v1.placeholder(tf.float32, shape=(None, 1), name='y-input')

# 定义神经网络的传播过程：
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播算法,tf.log tf.math.log
y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(y_*tf.math.log(
    tf.clip_by_value(y, 1e-10, 1.0))+(1-y)*tf.math.log(tf.clip_by_value(1-y, 1e-10, 1.0)))
# 定义学习率0.001
# 定义反向传播算法优化神经网络中的参数
# train.AdamOptimizer
train_step = tf.compat.v1.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 通过随机数生成一个模拟数据集
rdm = numpy.random.RandomState(1)
datatest_size = 128
X = rdm.rand(datatest_size, 2)

# 定义一个规则给出样本标签，所有x1+x2<1的样例都被认为使正样本（如零件合格）
# 其他样本为负样本，这里0表示负样本，1表示正样本，大部分分类问题的神经网络都用0和1表示方法
Y = [[int(x1+x2 < 1)]for (x1, x2) in X]

# 创建会话来运行 TensorFlow
with tf.compat.v1.Session() as sess:
    init_op = tf.compat.v1.global_variables_initializer()

    # 初始化变量
    sess.run(init_op)
    print(sess.run(w1))
    print(sess.run(w2))
    # 训练之前神经网络参数的值

    # 设定训练轮数
    STEPS = 5001
    for i in range(STEPS):
        # 每次选取batch_size个样本进行训练
        start = (i*batch_size) % datatest_size
        end = min(start+batch_size, datatest_size)
        # 通过选取的样本训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 1000 == 0:
            # 每隔一段时间计算所有的数据上的交叉熵并输出u
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
            print('after %d training step(s),cross entropy on all data is %g' % (i, total_cross_entropy))
# print(sess.run(w1))
# print(sess.run(w2))
