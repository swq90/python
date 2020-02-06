import tensorflow as tf

import numpy as np

x = tf.linspace(-8.,8,100) # 设置 x 坐标的间隔
y = tf.linspace(-8.,8,100) # 设置 y 坐标的间隔
x,y = tf.meshgrid(x,y) # 生成网格点，并拆分后返回
print(x.shape,y.shape) # 打印拆分后的所有点的 x,y 坐标张量 shape


a=tf.random.normal([4,12,8])
b=tf.random.normal([6,12,8])
c=tf.concat([a,b],axis=0)

print(c.shape)


x=tf.constant([1,2,3,4])
print(x.shape)
x=tf.expand_dims(x,axis=0)
x=tf.expand_dims(x,axis=-1)

print(x.shape)
print(x)
# x=tf.reshape(x,[2,-1])
x=tf.tile(x,multiples=[1,1,2])
print(x.shape)
print(x)
z=tf.random.normal([2,4,4,3])
print(z[0])
print(z[0][2][1])
print(z[0,2,1,2])

layer=tf.keras.layers.Conv2D(16,kernel_size=3)
out=layer(z)
print(z)
print(out.shape)