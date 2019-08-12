import tensorflow as tf
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([3.0, 4.0], name="b")
result = tf.add(a, b, name="add")
print(result)


# Tensor("add:0", shape=(2,), dtype=float32)
# TensorFlow 计算 的结果不是一个具体的数字， 而且一个张量的结构。从上面代码的运行结果可以看出， 一 个张量中主要保存了三个属性：
# 名字（name）、维度（shape）和类型（type）。
# 在 3.1.2 节中介绍了 TensorFlow 的计算都可以通过计算图的模型来建立， 而计算图上的每一个节点代表了一个计算，计算的结果就保存在张量之中。
# 所以张量和计 算图上节点所代表的计算结果是对应的。这样张量的命名就可以通过 “node:src_output”的 形式来给出。
# 其中 node 为节点的名称， src一output 表示当前张量来自节点的第几个输出。 比如上面代码打出来的“add：。”就说明了 result 这个张量是计算节点“add” 输出的第一个 结果（编号从 O 开始）。
# “add：。”就说明了 result 这个张量是计算节点“add” 输出的第一个 结果（编号从 O 开始）。
# 张量的第二个属性是张量的维度（shape）。这个属性描述了一个张量的维度信息。
# shape=(2，）说明了张量 result 是一个一维数组， 这个数组的长度为 2。维度是
# 张量一个很重要的属性， 围绕张量的维度 TensorFlow 也给出了很多有用的运算，

# a = tf.constant([1,2],name="a")
# 上面回事a的类型默认为整数，，a+b会报类型不匹配
