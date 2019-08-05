#TensorFlow 入门
##3.1 TensorFlow计算模型——计算图
计算图时TensorFlow中最基本的一个概念，TensorFlow中所有计算都会转为计算图上节点的计算
###3.1.1计算图的概念
TensorFlow中，tensor张量可以被简单理解为多维数组；flow“流”表达了张量见通过计算相互转化的过程
TensorFlow 是一个通过计算图的形式来表述计算的编程系统。 
TensorFlow 中的每一个计算都是计算图上的一个节点，而节点之间的边描述了计算之间的依赖关系。
###3.1.2计算图的使用
TensorFlow 程序一般可以分为两个阶段。  
####第一个阶段需要定义计算图中所有的计算。
```
import tensorflow as tf

a = tf.constant([1.0,2.0], name="a")
b = tf.constant([2.0,3.0], name="b")
result = a+b
``` 
在 TensorFlow 程序中，系统会自 动维护一个默认的计算图，通过 tf.get_default_graph 函数可以获取当前默认的计算图 
除了默认的计算图，TensorFlow支持通过tf.Graph生成新的计算图
不同计算图上张量和运算都不会共享
```python
import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    #在计算图g1中定义变量“v”，并设置初始值为0
    #v = tf.get_variable("v",initializer=tf.zeros_initializer(shape=[1]))
    #旧版，已弃用，更新为下
    #v = tf.compat.v1.get_variable("v",initializer=tf.zeros_initializer(shape=[1]))
    #报错：init__() got an unexpected keyword argument 'shape'
    #       return func(*args, **kwargs)
    #shape
    v = tf.compat.v1.get_variable("v",initializer=tf.zeros_initializer()(shape=[1]))

g2 = tf.Graph()
with g2.as_default():
    #在计算图g1中定义变量“v”，并设置初始值为1
    #v = tf.get_variable("v",initializer=tf.ones_initializer(shape=[1]))
    #v = tf.compat.v1.get_variable("v",initializer=tf.ones_initializer(shape=[1]))
    v = tf.compat.v1.get_variable("v",initializer=tf.ones_initializer,shape=[1])
    #两种shape有什么差别？
#在计算图g1中读取变量“v”的值
with tf.compat.v1.Session(graph=g1) as sess:
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("",reuse=True):
        #在计算图g1中，变量v的取值应该为0，所以下面会输出[0.]
        print(sess.run(tf.compat.v1.get_variable("v")))

with tf.compat.v1.Session(graph=g2) as sess:
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("",reuse=True):
        print(sess.run(tf.compat.v1.get_variable("v")))
```

有效地整理TensorFlow程序中的资源也是计算图的一个重要功能  
可以通过集合（collection）来管理不同类别的资源  

TensorFlow中维护的集合列表

|集合名称|集合内容|集合列表|
|:------|:------|:------|
|tf.GraphKeys. VARIABLES|所有变量 |持久化 TensorFlow 模型|
|tf.GraphKeys.TRAINABLE_VARIABLES|可学习的变量（一般指神经网络中的参数）|模型训练、生成模型可视化内容|
|tf.GraphKeys.SUMMARIES |日志生成相关的张量| TensorFlow 计算可视化|
|tf.GraphKeys.QUEUE _RUNNERS|处理输入的QueueRunner |输入处理|  
|tf.GraphKeys.MOVING_AVERAGE_VARIABLES |所有计算了滑动平均值的变量|计算变量的滑动平均值|


####第二个阶段为执行计算。 
##TensorFlow数据模型——张量
###张量
所有的数据都通过张量的形式来表示。从功能的角度上看，张量可以被简单理解为多维数组。  
其中零阶张量表示标量（scalar），也就是一个数（张量的类型也可以是字符串）；
第一阶张量为向量 Cvector), 也就是一个一维数组；
第 n 阶张量可以理解为一个 n 维数组。  
但张量在TensorFlow中的实现并不是直接采用数组的形式，它只是对 TensorFlow 中**运算结果的引用**。它保存的是**如何得到这些数字的计算过程**
```python
import tensorflow as tf
a = tf.constant([1.0,2.0],name="a")
b = tf.constant([1.0,2.0],name="a")
result = tf.add(a,b,name="add")
print(result)
#输出：
#Tensor("add:0", shape=(2,), dtype=float32)
```
三个属性：名字，维度，类型  
名字：不仅是一个张量的唯一标识符， 它同样也给出了这个张量是如何计算出来的     
    “add:0”说明result这个张量是计算节点“add”输出的第一个结果（编号从0开始）  
    （TensorFlow的计算都可以通过计算图的模型来确立，而图上的每一个节点代表一个计算。所以张量和计算图上的节点是对应的。张量的命名就可以通过“node:src_output”的形式给出。node为节点名称，src_output是当前节点的第几个输出）  
维度：shape(2,)说明result是一维数组，长度为2。重要属性，TensorFlow中有许多围绕张量维度的计算  
类型：每个张量的类型是唯一的。运算前会对类型进行检查   
可以使用dtype指定类型，避免默认类型出错：  
>a ＝ tf.constant([l, 2], name="a” , dtype=tf.float32)”

###3.2.2张量的使用
和TensorFlow的计算模型相比，它的数据模型相对简单
张量的使用主要分为两类：
####对中间计算结果的引用
当一个计算中包含很多中间结果时，使用张量可以提高代码可读性

