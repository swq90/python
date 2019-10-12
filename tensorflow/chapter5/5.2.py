import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# MNIST数据相关的数。
INPUT_NODE = 784  # 输入层的节点数。对于MNIST数据集，这个就等于图片的像素。
OUTPUT_NODE = 10  # 输出层的节点数。这个等于类别的数目。因为在MNIST数据集叶# 市要区分的足O～9这10个数宇，所以这里输出层的节点数为10。

# 配置神经网络的参数。
# 输出层的节成数。这个等于类别的数目。因为在MNIST数据集叶# 市要区分的足O～9这10个数宇，所以这里输出层的节点数为10。
# 隐藏层节点数。这里使用只有一个隐藏层的网络结构作为样例。
# 这个隐藏层有500个节点。
BATCH_SIZE = 100
# 一个训练batch中的训练数据个数。数字路小时，训｜陈过程越接近# 随机梯度下降：数字越大时，训练、越接近梯度下降。
LEARNING_RATE_BASE = 0.8  # 基础的学习率。
LEARNING_RATE_DECAY = 0.99  # 学习率的衰减率。
LAYER1_NODE = 500
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 30000
MOVING_AVERAGE_DECAY = 0.99


# 描述模型复杂度的正则化项在损失函数中的系数。
# 训练轮数。
# 滑动平均衰减率。
# 一个辅助函数，给定神经网络的输入和所有参数，计算神经网络的前向传播结果。在这里
# 定义了一个使用ReLU激活函数的三层全连接神经网络。通过加入隐藏层实现了多层网络结构，
# 通过ReLU激活函数实现了去线性化。在这个函数中也支持传入用于计算参数平均值的类，
# 这样方便在测试时使用滑动平均模型。
def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    # 当没有提供滑动平均类时，直接使用参数当前的取值。
    if avg_class == None:
        # 计算隐藏层的前向传播结果，这里使用了ReLUi版活函数。
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)
        # 计算输出层的前向传播结果。因为在计算损失函数时会并计算softmax函数，
        # 所以这里不需要加入激活函数。而且不加入softmax不会影响预测结果。因为预测时
        # 使用的是不同类别对应节点输出值的相对大小，有没有softmax层对最后分类结果的
        # 计算没有影响。于是在计算整个神经网络的前向传播时可以不加入最后的softmax层。
        return tf.matmul(layer1, weights2) + biases2

        #
    else:
        # 首先使用avgclass.average函数来计算得出变量的滑动平均值，
        # 然后再计算相应的神经网络前向传播结果。
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) +
                            avg_class.average(biases1))
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)


# 训练模型的过程。
def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')
    # 生成隐藏层的参数。
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))
    # 生成输出层的参数。
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))
    # 计算在当前参数下神经网络前向传播的结果。这里给出的用于计算滑动平均的类为None,
    # 所以的数不会使用参数的滑动平均值。
    y = inference(x, None, weights1, biases1, weights2, biases2)
    # 定义在储训练轮数的变旺。这个变盘不需要计算滑动平均值，所以这里指定这个变量为
    # 不可训练的变量（trainable=Fasle）。在使用TensorFlow训练神经网络时，
    # －般会将代友训练轮数的变量指定为不可训练的参数。
    global_step = tf.Variable(0, trainable=False)

    # 给定消动平均哀减率和训练轮数的变茧，初始化滑动平均类。在第4章中介绍过给
    # 定训练轮数的变量可以JJ~i快训练早期变量的更新速度。
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # 在所有代友神经网络参数的变盘上使用滑动平均。其他辅助变量（比如global_step）就
    # 不需要了。tf.trainablevariables返回的就是图上集合
    # GraphKeys.TRAINABLEVARIABLES中的元索。这个集合的元索就是所有没有指定
    # trainable=False的参数。
    variables_averages_op = variable_averages.apply(tf.trainable_variables())
    # 计算使用了滑动平均之后的前向传播结果。第4章巾介绍过滑动平均不会改变变fil本身的取值
    # 而是会维护一个澎子变量来记正式其滑动平均值。所以当面要使用这个滑动平均值时，
    # 需要明确调用average函数。
    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)
    # 计算交叉；胸作为刻画顶训值和真实值之间差距的损失函数。这里使用了TensorFlow中提
    # 供的sparse_softmax_cross_entropy_with_log工ts函数来计算交叉焰。当分类
    # 问题只打一个正确答案时，可以使用这个函数来加速交叉娟的计算。MNIST问题的图片中
    # #n包含了。～9巾的－个数字，所以可以使用这个函数来计算交叉娟损失。这个函数的第一个
    # 参数丛书Ji经网络不包括softmax层的前向传播结果，第二个是训练数据的正确答案。因为
    # 标准干年来是a个氏度为10的一维数组，而该函数需要提供的是一个正确答案的数字，所以需要
    # 使用tf.argmax函数来得到正确答案对应的类别编号。
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y, 1))
    # 计算在、＂1前batch中所有样例的交叉娟平均值。
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    # 计算12正则化损失函数。
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    # 一般只计算神经网络边上权重的正则化损失，而不使用伺。
    regularization = regularizer(weights1) + regularizer(weights2)
    # 总损失悖于交叉悄损失利正则化损失的利。
    loss = cross_entropy_mean + regularization
    # 设咒指数衰减的学习率。

    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step, mnist.train.num_examples / BATCH_SIZE,
                                               LEARNING_RATE_DECAY)
    # 基础的学习率，随着法代的进行，旦新变盐｜付使用的
    # 学习率在这个基础上递减。
    # 当前途代的轮数。
    # 过完所有的训练数据南耍的法# 代次数。
    # 学习率衰减速度。
    # 使用tf.train.GradientDescentOptimizer优化算法来优化损失函数。注意这里损失函数

    # 包含了交叉；脑损失和12正则化损失。
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    # 在训练、神经网络模型时，每过一遍数据既需要通过反向传播来更新神经网络中的参数，
    # 又要更新每一个参数的滑到J平均值。为了一次完成多个操作，TensorFlow提供了
    # tf.controldependencies和tf.group两种机制。下面两行程序和l
    # train_op=tf.group(train_step,variables_averages_op）是等价的。
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')
    # 检验使用了滑动平均模型的神经网络前向传播结果是否正确。tf.argmax(average_y,1)
    # 计算每一个样例的预测答案。其中average_y是一个batch_size食10的二维数组，每一行
    # 表示一个样例的前向传播结果。tf.argmax的第二个参数＂l”表示选取最大值的操作仅在第一
    # 个维度中进行，也就是说，只在每一行选取最大值对应的下标。于是得到的结果是一个长度为
    # batch的一维数组，这个一维数组中的值就表示了每一个样例对应的数字识别结果。tf.equal
    # 判断两个张量的每一维是否相等，如果相等返回True，否则返回False。
    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    # 这个运算首先将一个布尔型的数值转换为实数型，然后计算平均值。这个平均值就是模型在这
    # 一组数据上的正确率。
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 初始化会话并开始训练过程。
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        # 准备验证数据。一般在神经网络的训练过程中会通过验证数据来大致判断停止的
        # 条件和评判训练的效果。
        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
        # 准备测试数据。在真实的应用中，这部分数据在训练时是不可见的，这个数据只是作为模
        # 型优劣的最后评价标准。
        test_feed = {x: mnist.test.images, y_: mnist.test.labels}
        # 迭代地训练神经网络。
        for i in range(TRAINING_STEPS):
            # 每1000轮输出一次在验证数据集上的测试结果。
            if i % 1000 == 0:
                # 计算滑动平均模型在验证数据上的结果。因为MNIST数据集比较小，所以一次
                # 可以处理所有的验证数据。为了计算方便，本样例程序没有将验证数据划分为更
                # 小的batch.当神经网络棋型比较复杂或者验证数据比较大时，太大的batch
                # 会导致计算时间过长甚至发生内存溢出的错误。
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print("After %d training step(s),validation accuracy "
                      "using average model is %g" % (i, validate_acc))
                # 产生这一轮使用的一个batch的训练、数据，并运行训练过程。
                xs, ys = mnist.train.next_batch(BATCH_SIZE)
                sess.run(train_op, feed_dict={x: xs, y_: ys})
            # 在训练结束之后，在测试数据上检测神经网络模型的最终正确率。
            test_acc = sess.run(accuracy, feed_dict=test_feed)
            print("After %d training step(s),test accuracy using average model "
                  "is %g" % (TRAINING_STEPS, test_acc))


# 主程序入口。

def main(argv=None):
    # 声明处理MNIST数据集的类，这个类在初始化时会自动下载数据。
    mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
    train(mnist)


# TensorFlow提供的一个主程序入口，tf.app.run会调用上面定义的main函数。
if __name__ == '__main__':
    tf.app.run()