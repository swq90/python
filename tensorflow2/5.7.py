import tensorflow as tf
from tensorflow import keras
from keras import datasets

# 加载数据集
(x, y), (x_test, y_test) = datasets.mnist.load_data()
print('x', x.shape, 'y', y.shape, 'x-test', x_test.shape, 'y_test', y_test.shape)

# 数据加载后，药转换成Dataset对象

train_db = tf.data.Dataset.from_tensor_slices((x, y))

# print(train_db)

# 随机打散
# Dataset.shuffle(buffer_size),buffer_size 指定缓冲池大小，设置一个较大的参数即可
# Dataset提供工具返回新dataset对象，处理过程：
# db=db.shuffle().step2().step3()
train_db = train_db.shuffle(10000)

# 批训练
# 设置批训练方式
train_db = train_db.batch(128)


# 预处理
# 使数据集格式等满足模型的输入要求dataset提供map(func)
# datasets.batch()后，x.shape [b,28,28],像素使用0-255表示，y.shape [b]
# 神经网络输入，一般图片数据标准化到[0,1],[-1,1]等0附近的区间，根据网络设置也要将shape[28,28] reshape为合法的ing是，标注y可以变为one-hot编码，也可以计算误差时进行one-hot编码

# 将图片数据映射到[0,1]区间，shape调整为[b,28*28],标注y,进行one-hot编码
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32) / 255.
    x = tf.reshape(x, [-1, 28 * 28])  # 打平
    y = tf.cast(y, dtype=tf.int32)
    y = tf.one_hot(y, depth=10)
    return x, y


train_db = train_db.map(preprocess)

#循环训练
# 一般把完成一个batch训练叫做一个step，通过多少step完成训练集的依次迭代，叫做一个epoch，通常要进行多个epoch才能得到好的训练效果
# dataset对象可直接迭代，带step参数
#或者设置
#train_db=train_db.repeat(20)
for epoch in range(20):
    # for x,y in train_db:
    #     pass
    #或
    for step ,(x,y) in enumerate(train_db):
        #训练ing
        if step %100==0:
            print(step,'loss',float(loss))
        pass

