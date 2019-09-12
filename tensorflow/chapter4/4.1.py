import tensorflow as tf

w1 = tf.Variable(tf.random.normal([2, 3],stddev=1, seed=1))
w2 = tf.Variable(tf.random.normal([3, 1],stddev=1, seed=1))

x = tf.compat.v1.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.compat.v1.placeholder(tf.float32, shape=(None, 1), name='y-input')

a= tf.nn.relu (tf.matmul(x, w1) + biases1)
y = tf.nn.relu(tf.matmul(a, w2) + biases2)


#交叉熵
cross_entropy = -tf. reduce_mean( y_* tf.log(tf.clip_by_value(y, le-10, 1.0)))


# 1.tf.clip_by_ value 函数可以将一个张量中的 数值限制在一个范围之内
v = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0,6.0]])
print(tf.clip_by_value(v, 2.5, 4.5).eval())
# 输出［［ 2 .5 2 . 5 3.] [ 4. 4 . 5 4.5]]


# 2.tf.log 函数，这个函数完成了对张量中所有元素依次求对数 的功能
v = tf. constant ( [ 1.0, 2.0, 3.0])
print(tf.log(v) . eval())
# 输出［ 0. 0.69314718 1.09861231]

# 3.是乘法，在实现交叉娟的代码中直接将两个矩阵通过“＊”操作相乘。这个 操作不是矩阵乘法，而是元素之间直接相乘。矩阵乘法需要使用 tf.matmul 函数来完成。
vl = tf.constant([[1.0, 2.0], [3.0, 4.0]])
v2 = tf.constant([[5.0, 6.0], [7.0, 8.0]])
print (vl * v2) . eval ()
# 输出［［ 5 . 12 .] [ 21. 32 .] )
print(tf.matmul(vl , v2) . eval())
# 输出［［ 19 . 22.) [ 43. 50.)

# 以下代码简单展示了 tf.reduce_mean 函数的使用方法。
v = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(tf. reduce_mean (v) . eval () )

# 通过以下代 码来实现使用了 softmax 回归之后的交叉熵损失函数：
# y 代表了原始神经网络的输出结果，而 y_给出了标准答案。 这样通过一个命令就 可以得到使用了 Softmax 回归之后的交叉摘。在只有一个正确答案的分类问题中， Tensor Flow 提供了 tf.nn.sparse_ s。如nax_cross_ entropy_ with _logits 函数来进一步加速计

cross_entropy= tf.nn.softmax_cross_entropy_with_logits( labels=y_, logits=y)

loss= tf.reduce sum(tf . where(tf.greater(v1 ，v2) , (v1-v2) * a , (v2 - vl) * b))