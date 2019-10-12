import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

# 载入 MNIST 数据集，如果指定地址／path/to/MNIST data 下没有已经下载好的数据
# 那么 TensorFlow 会自动从表 5-1 给出的网址下载数据。
# 地址转义 r
mnist = input_data. read_data_sets(r"\Users\wqsha\Downloads", one_hot=True)
# 打印 Training data size : 55000 。
print("Training data size:", mnist.train.num_examples)
# 打印 Validating data size : 5000 。
print("Validating data size ：", mnist.validation.num_examples)
# 打印 Testing data size: 10000。
print("Testing data size:", mnist.test.num_examples)
# 打印Example training data : [ 0 . 0 . 0 . 0 . 380 0 . 376 .. 0. ].
print("Example training data :", mnist.train.images[0])
# 打印Example training data label:
# [ 0. 0. 0. 0. 0 . 0 . 0 . 1. 0 . O. ]
print("Example training data label :", mnist.train.labels[0])

#
# WARNING:tensorflow:From <ipython-input-2-693b414fbaac>:3: read_data_sets (from tensorflow.contrib.learn.python.learn.datasets.mnist) is deprecated and will be removed in a future version.
# Instructions for updating:
# Please use alternatives such as official/mnist/dataset.py from tensorflow/models.


batch_size = 100
xs, ys = mnist.train.next_batch(batch_size)
# 从 train 的集合中选取 batch size 个训练数据。
print("x shape:", xs.shape)
# 输出 x shape: (100, 784 ）。
print("Y shape :", ys.shape)
# 输出 Y shape: (100, 10)