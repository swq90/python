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

在 TensorFlow 中，不是所有的操作都可以被放在GPU上，如果强行将无法放在GPU上的操作指定到GPU上，那么程序将会报错。
在 TensorFlow 的kernel中定义了哪些操作可以跑在GPU上。
TensorFlow 在生成会话时可以指定allow_soft_placement参数。当allow_soft_placement参数设置为True时，如果运算无法由GPU执行，那么TensorFlow会自动将它放到CPU上执行
```python
import tensorflow as tf

a_cpu = tf.Variable(0, name='a_cpu')
with tf.device('/gpu:0'):
    a_gpu = tf.Variable(0, name='a_gpu')
# 通过 allow_soft_placement参数自动将无法放在GPU上的操作放回CPU
sess = tf.compat.v1.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=True))
sess.run(tf.initialize_all_variables())

```
一般来说不会把所有的操作全部放在GPU上。一个比较好的实践是将计算密集型的运算放在GPU上，而把其他操作放到CPU上。
GPU是机器中相对独立的资源，将计算放入或者转出GPU都需要额外的时间。而且GPU需要将计算时用到的数据从内存复制到GPU设备上，这也需要额外的时间。TensorFlow可以自动完成这些操作而不需要用户特别处理，但为了提高程序运行的速度，用户也需要尽量将相关的运算放在同一个设备上。

TensorFlow默认会占用设备上的所有GPU以及每个GPU的所有显存。如果在一个TensorFlow程序中只需要使用部分GPU，
可以通过设置CUDA_VISIBLE_DEVICES环境变量来控制
```
# 只使用第二块GPU(GPU编号从0开始）。在demo_code.py中，机器上的第二块GPU的名称变成／gpu:0，不过在运行时所街／gpu:0的运算将被放在第二块GPU上。
CUDA_VISIBLE_DEVICES=1 python demo_code.py
# 只使用第一块和第二块GPU
CUDA_VISIBLE_DEVICES=0,1 python demo_code.py
```
TensorFlow也支持在程序中设置环境变量
```python
import os

# 只用第三块GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "2"

```
虽然TensorFlow默认会一次性占用一个GPU的所有显存，但是TensorFlow也支持动态分配GPU的显存，使得一块GPU上可以同时运行多个任务  

```python
import tensorflow as tf


config = tf.ConfigProto()
#让tensorflow按需分配显存

config.gpu_options.allow_growth = True

# 或者直接按固定的比例分配，以下代码会占用所有可使用GPU的40%现存
# config.gpu_options.per_process_gpu_memory_fraction = 0.4
session = tf.compat.v1.Session(config=config, )

```
##12.2 深度学习训练并行模式

TensorFlow 可以很容易地利用单个GPU加速深度学习模型的训练过程，但要利用更多的GPU或者机器，需要了解如何并行化地训练深度学习模型
常用的并行化深度学习模型训练方式有两种，同步模式和异步模式
根据当前参数的取值和随机获取的一小部分训练数据，不同设备各自运行反向传播的过程并独立地更新参数。
异步模式就是单机模式复制了多份，每一份使用不同的训练数据进行训练。在异步模式下，不同设备之间是完全独立的。

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