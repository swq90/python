import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant([1.0,2.0], name="a")
b = tf.constant([2.0,3.0], name="b")
result = a+b
tf.get_default_graph
sess = tf.compat.v1.Session()
#要输入结果不能直接输出result，需要先生成一个会话（session），并通过会话计算结果
#新版本中写法如上
# I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
#解决上面编码警告：安装ignore包
print(sess.run(result))