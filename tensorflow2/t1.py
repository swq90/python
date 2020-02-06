import os
import tensorflow as tf
from tensorflow import keras
# (x,y),(x_val,y_val)=tf.keras.datasets.mnist.load_data()
# x=2*tf.convert_to_tensor(x,dtype=tf.float32)/255.-1
# y=tf.one_hot(y,depth=10)
# print(x.shape,y.shape)
# train_dataset=tf.data.Dataset.from_tensor_slices((x,y))
# train_dataset=train_dataset.batch(512)
x=tf.random.normal([4,28*28])
fc=keras.layers.Dense(512,activation=tf.nn.relu)
h1=fc(x)
w=fc.kernel
b=fc.bias
v=fc.trainable_variables#待优化参数列表
va=fc.variables#返回所有参数列表
