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
```python
import tensorflow as tf

a = tf.compat.v1.constant([1.0,2.0], name="a")
b = tf.compat.v1.constant([2.0,3.0], name="b")
result = a+b
print(tf.compat.v1.get_default_graph())
``` 
在 TensorFlow 程序中，系统会自动维护一个默认的计算图，通过 tf.compat.v1.get_default_graph 函数可以获取当前默认的计算图 
除了默认的计算图，TensorFlow支持通过tf.Graph生成新的计算图,不同计算图上张量和运算都不会共享
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
    #session,先生成一个会话，通过会话计算结果
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("",reuse=True):
        #在计算图g1中，变量v的取值应该为0，所以下面会输出[0.]
        print(sess.run(tf.compat.v1.get_variable("v")))

with tf.compat.v1.Session(graph=g2) as sess:
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("",reuse=True):
        print(sess.run(tf.compat.v1.get_variable("v")))
        
g = tf.Graph()
# 指定计算运行设备
with g.device('/gpu:0'):
    a = tf.compat.v1.constant([1.0,2.0], name="a")
    b = tf.compat.v1.constant([2.0,3.0], name="b")
    result = a+b
```

计算图可以通过 tf.Graph.device 函数来指定运行计算的设 备。这为 TensorFlow 使用 GPU 提供了机制。
有效地整理TensorFlow程序中的资源也是计算图的一个重要功能  
可以通过集合（collection）来管理不同类别的资源  


TensorFlow中维护的集合列表  
|集合名称|集合内容|集合列表|  
| :-----| ----: | :----: |  
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
a = tf.compat.v1.constant([1.0,2.0],name="a")
b = tf.compat.v1.constant([1.0,2.0],name="b")
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
    类型：每个张量的类型是唯一的。运算前会对类型进行检查,可以使用dtype指定类型，避免默认类型出错：  
```
a ＝ tf.constant([l, 2], name="a” , dtype=tf.float32)”
```
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
# 设置默认会话计算张量
sess = tf.compat.v1.Session()
with sess.as_default():
    print(result.eval)
```
以下代码完成相同的功能
```
sess = tf.Session()

#上下两个命令具有相同的功能
print(sess.run(result))
print(result.eval(session=sess))
```

交互环境下，设置默认会话的方式获取张量的取值更加方便
在交互式环境下直接构建默认会话的函数 tf.compat.v1.InteractiveSession，将自动生成的会话注册为默认会话  
```
#省去了将产生会话注册为默认会话的过程
sess = tf.c
InteractiveSession()
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
sess2 = tf.Session(config=config)
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
全连接：相邻两层之间任意两个节点之间都有连接   
向前传播结果需要三部分信息：   
    神经网络的输入：实体中提取的特征向量
    神经网络的连接结构：神经元之间输入输出的连接关系，神经元也可以说是节点
    每个神经元的参数：W，也可以说是权重


W可以组成矩阵，然后利用矩阵的乘法
    
    a=tf.matmul(x,w1)
    y=tf.matmul(a,w2)


    
###3.神经网络参数及tg变量  
参数是神经网络实现分类或者回归问题中重要的部分。  
TensorFlow 是如何组织、保存以及使用神经网络中的参数   
变量（tf. Variable）的作用就是保存和更新神经网络中的参数   
变量也需要指定初始值。因为在神经网络中，给参数赋予随机初始值最为常见，所以一般也使用随机数给TensorFlow中的变量初始化  
声明一个2*3的矩阵变量：
    weights = tf.Variable(tf.random_normal([2,3],stddev=2))
产生一个2*3的矩阵，元素均值0，标准差为2的随机数，可以通过mean来指定平均值，默认为0
tf的变量初始值可以设置成随机数，常熟，或者通过其他变量的初始值得到  
    tf.zeros([2,3],int32)->[[0,0,0],[0,0,0]]
    tf.ones([2,3],int32)->[[0,0,0],[0,0,0]]
    tf.fill([2,3],9)->[[9,9,9],[9,9,9]]
    tf.constant([1,2,3])->[1,2,3]  
 
偏置项bias同行会使用常熟来设置初始值   
    biases = tf.Variable(tf.zeros([3])) 

TensorFlow 也支持通过其他变量的初始值来初始化新的变量。
    w2 = tf.Variable(weights.initialized_value()) 
    w3 = tf.Variable(weights.initialized_value()*2.0) 
    
tf中，变量的值在使用前，变量的初始化过程要被明确的调用
    sess.run(w1.initializer)#初始化w1
变量较多或者存在依赖关系时，单个调用很麻烦，可以通过：tf.global_variables_initializer实现初始化所有变量
    init_op = tf.global_variables_initializer()
    sess.run(init_op)  
    
数tf.Variable是一个运算。这个运算的输出结果就是一个张量所以变量只是一种特殊的张量
初始化变量的操作是通过Assign操作完成

tf.global_variables()函数可以拿到当前计算图上的所有变量  
通过 tf.global_variables（）函数可以拿到当前计算图 上所有的变量。拿到计算图上所有的变量有助于持久化整个计算图的运行状态，在第 5 章 中将更加详细地介绍。当构建机器学习模型时，比如神经网络，可以通过变量声明函数 中的 trainable 参数来区分需要优化的参数（比如神经网络中的参数）和其他参数（比如 选代的轮数）。如果声明变量时参数 trainable 为 True ，那么这个变量将会被加入到
GraphKeys. TRAINABLE_ V ARJABLES 集合。在 TensorFlow 中可以通过 tf.trainable_variables 函数得到所有需要优化的参数 。 TensorF!ow 中提供的神 经网络优化算法会将 GraphKeys.TRAINABLE_ VARIABLES 集合中的变量作为默认的优化对象  
 
维度shape类型type是变量的两个重要属性，变量构建后类型就不能再改变了
 
###4.通过tf训练神经网络模型  
设置神经网络参数的过程就是神经网络的训练过程，只有经过有效训练的神经网络模型才可以真正地解决分类或者回归问题。   
使用监督学习的方式设置神经网络参数需要有一个标注好的训练数据集  
神经网络优化算法，常用的反向传播算法 backpropagation  
神经网络反向传播流程图：
    选取一小部分训练数据，batch
    batch经过向前传播算法得到神经网络模型的预测结果，（训练数据有正确答案标注）
    基于预测值和真实值，反向传播算法更新神经网络参数取值，使在当前batch上预测与真实结果更接近
    
为避免每轮迭代数据都要通过常量表示（计算图太大）tf中placeholder机制提供输入数据
placeholder相当于定义一个位置，这个位置中的数据在程序运行时再指定,它的维度信息可以根据提供的数据推到出，不一定必须给出  
在新的程序中计算前向传播结果时，需要提供一个feed_dict来指定 x 的取值。 feed_dict 是一个字典（map），在字典中需要给出每个用到的placeholder的取值

在得到一个batch的向前传播结果之后，需要定义一个损失函数来刻画当前预测值和真实答案之间的差距
然后通过反向传播算法来调整神经网络参数的取值，来缩小差距 sigmoid

使用sigmoid 函数将y转换为0～1之间的数值。转换后y代表预测是正样本的概率， 1-y 代表预测是负样本的概率。 
cross_entropy 定义了真实值和预测值之间的交叉熵（cross_entropy), 这是分类问题中一个常用的损失函数。第二行 train_step 定义了反向传播的优化方法
常用的优化方法有三种： tf.train. GradientDescentOptimizer 、 tf.train.AdamOptimizer 和 tf. train.MomentumOptimizer
###5.完整神经网络样例程序 
    神经网络的步骤：
    l. 定义神经网络的结构和前向传播的输出结果。 
    2. 定义损失函数以及选择反向传播优化的算法。 
    3. 生成会话（tf.Session）并且在训练、数据上反复运行反向传播优化算法。 
    无论神经网络的结构如何变化，这三个步骤是不变的 

tf.random.normal# tf.random_normal  
tf.compat.v1.placeholder#tf.placeholder
tf.compat.v1.train.AdamOptimizer# train.AdamOptimizer
##总结
计算图 (tf.Graph）、张量 (tf.Tensor）和会话（tf.Session）。
tf中，所有的计算都会转化为计算图上的节点，计算图时tf的激素墨西哥
数据模型——张量是tf管理数据的形式，
session则来执行定义好的运算
