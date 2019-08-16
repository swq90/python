#TensorFlow 入门
##3.1 TensorFlow计算模型——计算图
计算图时TensorFlow中最基本的一个概念，TensorFlow中所有计算都会转为计算图上节点的计算
###3.1.1计算图的概念
TensorFlow中，tensor张量可以被简单理解为多维数组；flow“流”表达了张量见通过计算相互转化的过程  
TensorFlow 是一个通过计算图的形式来表述计算的编程系统。   

TensorFlow 中的每一个计算都是计算图上的一个节点，而节点之间的边描述了计算之间的依赖关系。
###3.1.2计算图的使用

**a.graph,查看张量a所属计算图，没有指定下相当于默认计算图，tf.get_default_graph()
tf.Graph函数可生产新的计算图**

TensorFlow 程序一般可以分为两个阶段。  
####第一个阶段需要定义计算图中所有的计算。
```
#eg1
import tensorflow as tf

a = tf.constant([1.0,2.0], name="a")
b = tf.constant([2.0,3.0], name="b")
result = a+b
``` 
在 TensorFlow 程序中，系统会自动维护一个默认的计算图，通过 tf.get_default_graph 函数可以获取当前默认的计算图 
除了默认的计算图，TensorFlow支持通过tf.Graph生成新的计算图
不同计算图上张量和运算都不会共享
```python
#eg2
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
    #session,先生成一个会话，通过会话计算结果
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
#eg3
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
####a.对中间计算结果的引用 
当一个计算中包含很多中间结果时，使用张量可以提高代码可读性，如：
```
result = a+b
```
与直接计算向量的和相比，可读性更强；而且不用再去生成这些常量
通过张量来存储中间结果可以方便获取中间结果。 比如在卷积神经网络(chapter6)中：  
卷积层或者池化层有可能改变张量的维度，通过 result.get_shape 函数来获取结果张 量的维度信息可以免去人工计算的麻烦。 
####b.当计算图构造完成之后，张量可以用来获得计算结果

##3.3TensorFlow 运行模型——会话
会话，session来执行定义好的运算，拥有并管理tf程序运行时所有的资源  
所有计算完成后需要关闭会话来帮助系统回收资源，避免资源泄露  

两种会话模式：  
1.需要明确调用会话生成函数和关闭会话函数  
```
sess = tf.compat.v1.Session()
sess.run(result)
#关闭会话，本次运行中用到的资源可以被释放 
sess.close()
```
缺点：程序异常退出时，close()可能不会被执行导致资源泄露
老办法：
2.使用python上下文管理器
```
with tf.compat.v1.Session() as sess:
    sess.run(...)
```  


没有特殊指定，运算会自动加入tf自动生成的默认计算图中，而会话不能自动生成，要手动指定。当默认会话被指定后，可以通过tf.Tensor.eval函数计算一个张量的取值
```
sess = tf.Session()
with sess.as_defalut():
    print(result.eval)
```
以下代码完成相同的功能
```
sess = tf.Session()

#上下两个命令具有相同的功能
print(sess.run(result))
print(sess.eval(session=sess))
```
上面两段代码具有相同的功能

tf.InteractiveSession，在交互式环境下直接构建默认会话的函数   
```
#省去了将产生会话注册为默认会话的过程
sess = tf.InteractiveSession()
print(result.eval()) 
sess. close () 
```
可以用ConfigProto Protocol Buffer配置需要生成的会话：
并行线程数，GPU分配策略，运算超时时间参数，
allow_soft_placement,为True，以下任一条件成立，GPU运算放在CPU运行：

1. 运算无法在 GPU 上执行。 
2. 没有 GPU资源（比如运算被指定在第二个GPU上运行,但是机器只有一个GPU。
3. 运算输入包含对CPU计算结果的引用。

log_device _placement o 这也是一个布尔型的参数，当它为 True 时日志中将会记录每个节点被安排在哪个设备上以方便调试。而在生产环境中将这个参数设置为False可以减少日志量。

```
config = tf.ConfigProto(allow_soft_placement=True,log_device_placement=Trur)
sess1 = tf.InteractiveSession(config=config)
sess2 = tf.Session(config=config
```

##3.4TensorFlow实现神经网络
###1.tf游乐场及神经网络  
神经网络主要功能及计算流程  
在机器学习中，所有用于描述实体的数字的组合就是一个实体的特征向量（feature vector）。特征向量的提取对机器学习的效果至关重要   
特征向量是神经网络的输入   
神经网络主体结构，目前主流都是分层结构：  
    第一层是输入层，代表特征向量中每一个特征的取值  
    同层节点不会相互连接，而且每一层只和下一层连接，直到最后一层是输出层得到计算结果
    输入输出层之间的为隐藏层，一般隐藏层越多，神经网络越“深”  

tf游乐场支持选择神经网络的参数：深度，每层节点数，学习率，激活函数，正则化

游乐场结构中，节点间的连线代表参数（w，权重）颜色越深，参数绝对值越大，接近白色，取值接近0
而节点上的颜色代表这个节点的区分平面？点的颜色代表特征值，颜色同参数

神经网络就是通过对参数的合理设置来解决分类或回归问题
  



###2.向前传播算法  
向前传播算法及代码实现
最简单的全连接网络结构的向前传播算法：
    神经元结构：一个神经元有多个输入一个输出，神经网络的结构是不同神经元之间的连接结构   
神经网络优化的过程就是优化神经元中参数取值的过程
全连接：相邻零层之间任意两个节点之间都有连接  、


    
###3.神经网络参数及tg变量  
通过变量
###4.通过tf训练神经网络模型  
###5.完整神经网络样例程序  

##总结
tf中，所有的计算都会转化为计算图上的节点，数据模型——张量是tf管理数据的形式，而会话session则来执行定义好的运算