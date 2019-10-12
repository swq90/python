import tensorflow as tf
import numpy.random

batch_size = 8
# 两个输入节点
# 回归问题只有一个输出节点
x = tf.compat.v1.placeholder(tf.float32, shape=(None, 2), name="x-input")
y_ = tf.compat.v1.placeholder(tf.float32, shape=(None, 1), name="y-input")

# 向前传播过程，加权和
w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
y = tf.matmul(x, w1)

# 预测多或少的成本
loss_less = 10
loss_more = 1
loss = tf.reduce_sum(tf.where(tf.greater(y, y_), (y-y_)*loss_more, (y_-y)*loss_less))
# 反向传播的参数,学习率0.001，损失函数
train_step = tf.compat.v1.train.AdamOptimizer(0.001).minimize(loss)

# 生成模拟数据集
rdm = numpy.random.RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)

# 设置回归的正确值为两个输入的和加上一个随机量。
# 之所以要加上一个随机量是为了加入不可预测的噪音
# 否则不同损失函数的意义就不大了，因为不同损失函数都会在能完全预测正确的时候最低。
# 一般噪音为一个均值为 0 的小量，所以这里的噪音设置为-0.05～-0.05 的随机数。
Y = [[x1 + x2 + rdm . rand()/10.0-0.05] for (x1, x2) in X]


saver = tf.train.Saver()
# 训练神经网络
with tf.compat.v1.Session() as sess:
    init_op = tf.compat.v1.global_variables_initializer()
    sess.run(init_op)
    STEPS = 5000
    for i in range(STEPS):
        start = (i*batch_size) % dataset_size
        end = min(start+batch_size, dataset_size)
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        print(sess.run(w1))
        saver_path=saver.save(sess,"save/model.ckpt")



# 载入模型
saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, "save/model.ckpt")