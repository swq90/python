import tensorflow as tf
with tf.variable_scope("foo"):
# 在命名空间 foo 下获取变量“bar飞于是得到的变量名称为“foo/bar”。
    a = tf. get_variable ("bar",[1])
    print(a .name)
# 输出：foo/bar:0


with tf.variable_scope ("bar") :
# 在命名空间 bar 下获取变量“bar飞于是得到的变量名称为“bar/bar飞此时变豆 # “bar/bar＂和变量“foo/bar”并不冲突，于是可以正常运行。
    a = tf. get_variable ("bar",[1])
    print(a .name)
# 输出： bar/bar:O
with tf.name_scope("a"):
#使用 tf.Variable 函数生成变量会受 tf.name_scope 影响,于是这个变茧的名称 ＃为“a/Variable飞
    a = tf. Variable([1])
    print(a .name)

# tf.get_variable 函数不受 tf.name_scope 函数的影响，
# 于是变量并不在 a 这个命名空间中。
a = tf. get_variable("b", [1])
print(a.name)
# 输出 ： b :O
with tf.name_scope("b"):
# 因为 tf.get_variable 不受 tf . name_scope 影响，所以这里将试图获取名称 ＃为“a”的变量。然而这个变量己经被声明了，于是这里会报重复声明的错误：
# ValueError: Variable bar already exists, disallowed. Did you mea口 # to set reuse=True in VarScope? Originally defined at :
    tf.get_variable("b", [1])