#chapter12 TensorFlow计算加速
为了加速训练过程，TensorFlow利用GPU或／和分布式计算进行模型训练。
##12.1 tf使用GPU
TensorFlow程序可以通过tf.device函数来指定运行每一个操作的设备，这个设备可以是本地的CPU或者GPU也可以是某一台远程的服务器

tf.device 函数可以通过设备的名称来指定执 行运算的设备。比如 CPU 在 TensorFlow 中的名称为／cpu:0,默认下，所有的 CPU 都使用／cpu:0作为名称
同 GPU 的名称是不同的，第 n 个 GPU 在 TensorFlow 中的名称为也/gpu:n
在生成会话时，可 以通过设置 log_device _placement 参数来打印运行每一个运算的设备
TensorFlow 程序生成会话时加入了参数 log_device _placement=True, 所以程序会将运行每一个操作的设备输出到屏幕


```python
import tensorflow as tf
a= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'a')
b= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'b')
c = a + b
# 边过 log_device_placement 参数来输出运行每一个运算的设备。
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
print(sess . run(c))
# 在没有 GPU的机器上运行以上代码可以得到类似以下的输出 ：
# Device mapping: no known devices .
# add:(Add): /job:localhost/replica:O/task:O/cpu:O
# b : (Const): /job: localhost/replica: 0/task: 0/cpu: 0
# a : (Const): /job: localhost/replica: 0/task: 0/cpu : 0 [ 2 . 4 . 6 . ] ”

# 配置好GPU的机器上显示默认会优先将运送放在GPU

```
通过tf.compat.v1.device将运算指定到特定的设备上
```python
import tensorflow as tf

with tf.compat.v1.device('/cpu:0'):
    a= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'a')
    b= tf.compat.v1.constant([1.0, 2.0,3.0], shape=[3] , name= 'b')
with tf.compat.v1.device('/gpu:1'):
    c = a + b
# 边过 log_device_placement 参数来输出运行每一个运算的设备。
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
print(sess . run(c))
```

在 TensorFlow 中，不是所有的操作都可以被放在 GPU 上，如 果强行将无法放在 GPU 上的操作指定到 GPU 上，那么程序将会报错。
在 TensorFlow 的 kernel中定义了哪些操作可以跑在 GPU 上。
TensorFlow 在生成会话时可以指定 allow_soft _placement 参数。当 allow_soft_placement 参 数设置为 True 时，如果运算无法由 GPU 执行，那么 TensorFlow 会自动将它放到 CPU 上执 行
```python



```


##12.2 深度学习训练并行模式
#####
##12.3 多GPU并行
###
##12.4 分布式tf
###分布式tf原理
###分布式tf训练模型
##
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
###