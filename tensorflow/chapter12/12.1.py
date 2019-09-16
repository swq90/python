import tensorflow as tf
# a= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'a')
# b= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'b')
# c = a + b
# # 边过 log_device_placement 参数来输出运行每一个运算的设备。
# sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
# print(sess . run(c))
# # 在没有 GPU的机器上运行以上代码可以得到类似以下的输出 ：
# # Device mapping: no known devices .
# # add:(Add): /job:localhost/replica:O/task:O/cpu:O
# # b : (Const): /job: localhost/replica: 0/task: 0/cpu: 0
# # a : (Const): /job: localhost/replica: 0/task: 0/cpu : 0 [ 2 . 4 . 6 . ] ”


#
# with tf.device('/cpu:0'):
#     a= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'a')
#     b= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'b')
# with tf.device('/gpu:1'):
#     c = a + b
# # 边过 log_device_placement 参数来输出运行每一个运算的设备。
# sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
# print(sess . run(c))


a_cpu = tf.Variable(0, name='a_cpu')
with tf.device ('/gpu:0'):
    a_gpu = tf.Variable(0, name='a_gpu')
# 通过 allow_soft_placement参数自动将无法放在GPU上的操作放回CPU
sess = tf.compat.v1.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=True))
sess.run(tf.initialize_all_variables())
