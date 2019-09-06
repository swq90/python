import tensorflow as tf

a= tf.nn.relu (tf.matmul(x, wl) + biasesl)
y = tf.nn.relu(tf.matmul(a, w2) + biases2)


#交叉熵
cross_entropy = -tf. reduce_mean( y_* tf.log(tf.clip_by_value(y, le-10, 1.0)))


# tf.clip_by_ value 函数可以将一个张量中的 数值限制在一个范围之内
v = tf.constant([[l.0, 2.0, 3 .0], [4.0, 5.0,6 . 0]))
print tf.clip_by_value(v, 2.5, 4 . 5) . eval()
# 输出［［ 2 .5 2 . 5 3.] [ 4. 4 . 5 4.5]]


# tf.log 函数，这个函数完成了对张量中所有元素依次求对数 的功能
v = tf. constant ( [ 1. 0, 2 . 0, 3. 0]) print tf.log(v) . eval()
# 输出［ 0. 0.69314718 1.09861231]