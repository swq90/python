import tensorflow as tf


a = tf.compat.v1.constant([1.0,2.0], name="a")
b = tf.compat.v1.constant([2.0,3.0], name="b")
result = a+b
print(tf.compat.v1.get_default_graph())

g1 = tf.Graph()
with g1.as_default():
    #在计算图g1中定义变量“v”，并设置初始值为0
    #v = tf.get_variable("v",initializer=tf.zeros_initializer(shape=[1]))
    #旧版，已弃用，更新为下
    #v = tf.compat.v1.get_variable("v",initializer=tf.zeros_initializer(shape=[1]))
    #报错：init__() got an unexpected keyword argument 'shape'
    #       return func(*args, **kwargs)
    #shape 新写法
    v = tf.compat.v1.get_variable("v",initializer=tf.zeros_initializer()(shape=[1]))

g2 = tf.Graph()
with g2.as_default():
    #在计算图g1中定义变量“v”，并设置初始值为1
    #v = tf.get_variable("v",initializer=tf.ones_initializer(shape=[1]))
    #v = tf.compat.v1.get_variable("v",initializer=tf.ones_initializer(shape=[1]))
    v = tf.compat.v1.get_variable("v",initializer=tf.ones_initializer,shape=[1])
    #两种shape有什么差别？
#在计算图g1中读取变量“v”的值
with tf.compat.v1.Session(graph=g1) as sess:
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("",reuse=True):
        #在计算图g1中，变量v的取值应该为0，所以下面会输出[0.]
        print(sess.run(tf.compat.v1.get_variable("v")))

with tf.compat.v1.Session(graph=g2) as sess:
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("",reuse=True):
        print(sess.run(tf.compat.v1.get_variable("v")))