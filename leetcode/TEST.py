import tensorflow as tf
a = tf.compat.v1.constant([1.0,2.0],name="a")
b = tf.compat.v1.constant([1.0,2.0],name="b")
result = tf.add(a,b,name="add")
print(result)