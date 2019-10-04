import tensorflow as tf

v = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
with tf.Session() as sess:
    print(tf.reduce_mean(v).eval())


from numpy.random import RandomState

rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
X1= rdm.rand(2, 2)
Y = [[x1 + x2 + rdm . rand()/10.0-0.05] for (x1, x2) in X]
print(X1)
print(X1)
print(X1)
