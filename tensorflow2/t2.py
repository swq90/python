import tensorflow as tf
import numpy as np
z=tf.random.normal([2,4,4,3])
print(z[0])
print(z[0][2][1])
print(z[0,2,1,2])

layer=tf.keras.layers.Conv2D(16,kernel_size=3)
out=layer(z)
print(z)
print(out.shape)