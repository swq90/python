import tensorflow as tf
input1 = tf.constant([1.0, 2.0, 3.0], name='input1')
input2 = tf.compat.v1.Variable(tf.random.uniform([3]), name='input2')
output = tf.add_n([input1,input2],name='add')

# 生成一个写日志的writer,在当前tf计算图写入日志
writer = tf.compat.v1.summary.FileWriter("D:/workgit/python/tensorflow/log",tf.compat.v1.get_default_graph())
writer.close()

#生成文件