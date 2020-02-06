import tensorflow as tf
from tensorflow import keras

# from keras import layers
# 8.1.1
x = tf.constant([2., 1., 0.5])
layer = keras.layers.Softmax(axis=-1)
print(layer(x))

# 8.1.2网络容器

network = keras.Sequential(
    [keras.layers.Dense(3, activation=None), keras.layers.ReLU(), keras.layers.Dense(2, activation=None),
     keras.layers.ReLU()])
x = tf.random.normal([4, 3])
print(network(x))

# Sequential 容器也可以通过add()方法追加新网络层

layers_num = 2
network = keras.Sequential([])
for _ in range(layers_num):
    network.add(keras.layers.Dense(3))
    network.add(keras.layers.ReLU())
network.build(input_shape=(None,4))
network.summary()

 # 打印网络的待优化参数名与 shape
for p in network.trainable_variables:
    print(p.name, p.shape)
