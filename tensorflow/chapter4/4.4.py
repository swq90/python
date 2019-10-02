import tensorflow as tf
# 获取一层神经网络边上的权重，并将权重的L2正则化损失加入名称为losses的集合中

def get_weight(shape, lambd):
    #生成一个变量
    var = tf.compat.v1.Variable(tf.random_normal(shape),dtype=tf.float32)
    # add_to_collection函数将var的正则化损失项加入集合
    #参数：1，集合的名字，2，加入集合的内容
    tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(lambd)(var))
    # 返回生成的变量
    return var
