import tensorflow as tf
# import os
#
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant([1.0,2.0], name="a")
b = tf.constant([2.0,3.0], name="b")
result = a+b
#创建一个会话
# sess = tf.compat.v1.Session()
# sess.run(result)
#关闭会话，本次运行中用到的资源可以被释放
#sess.close()

#创建一个会话，使用python中上下文管理器管理该会话
with tf.compat.v1.Session as sess:
    sess.run()
#避免因异常退出时资源释放的问题