import os
import tensorflow as tf
from tensorflow import keras
(x,y),(x_val,y_val)=tf.keras.datasets.mnist.load_data()
x=2*tf.convert_to_tensor(x,dtype=tf.float32)/255.-1
y=tf.one_hot(y,depth=10)
print(x.shape,y.shape)
train_dataset=tf.data.Dataset.from_tensor_slices((x,y))
train_dataset=train_dataset.batch(512)
