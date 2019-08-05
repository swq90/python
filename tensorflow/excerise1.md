#Keras
##导入 tf.keras
```python
import tensorflow as tf
from tensorflow.keras import layers

print(tf.VERSION)#1.14.0
print(tf.keras.__version__)#2.2.4-tf
```
##构建简单模型
```python
model = tf.keras.Sequential()#1
# Adds a densely-connected layer with 64 units to the model:
model.add(layers.Dense(64, activation='relu'))
# Add another:
model.add(layers.Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(layers.Dense(10, activation='softmax'))
```
注释1处报错：
WARNING: Logging before flag parsing goes to stderr.
W0723 10:46:38.257865 12304 deprecation.py:506] From D:\workgit\venv\lib\site-packages\tensorflow\python\ops\init_ops.py:1251: calling VarianceScaling.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor