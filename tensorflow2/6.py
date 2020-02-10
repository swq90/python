import tensorflow as tf
from tensorflow import keras
from keras import layers

x=tf.random.normal([4,28*28])

model=layers.Sequential([layers.Dense(256,activation=tf.nn.relu),layers.Dense(128,activation=tf.nn.relu),layers.Dense(64,activation=tf.nn.relu),layers.Dense(10,activation=None)])

out=model(x)