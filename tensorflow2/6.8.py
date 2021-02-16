import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras

dataset_path = keras.utils.get_file("auto-mpg.data",
                                    "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
# 利用 pandas 读取数据集，字段有效能（公里数每加仑），气缸数，排量，马力，重量
# 加速度，型号年份，产地
column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
raw_dataset = pd.read_csv(dataset_path, names=column_names, na_values="?", comment='\t', sep=" ", skipinitialspace=True)
dataset = raw_dataset.copy()
print(dataset.shape)
dataset = dataset.dropna()
print(dataset.shape)
# 由于 Origin 字段为类别数据，我们将其移动出来，并转换为新的 3 个字段：USA， Europe 和 Japan，分别代表是否来自此产地：
# 处理类别型数据，其中 origin 列代表了类别 1,2,3,分布代表产地：美国、欧洲、日本 # 先弹出(删除并返回)origin 这一列
origin = dataset.pop('Origin')
dataset['USA'] = (origin == 1) * 1.0
dataset['Europe'] = (origin == 2) * 1.0
dataset['Japan'] = (origin == 3) * 1.0

# 切分为训练集和测试集
train_dataset = dataset.sample(frac=0.8, random_state=1)
test_dataset = dataset.drop(train_dataset.index)

train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

# 查看x的统计数据？
train_stats = train_dataset.describe()

train_stats = train_stats.transpose()


# 标准化数据
def norm(x):
    return (x - train_stats['mean']) / train_stats['std']


normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

print(normed_train_data.shape, train_labels.shape)
print(normed_test_data.shape, test_labels.shape)

# 利用切分的训练集数据构建数据集对象
train_db = tf.data.Dataset.from_tensor_slices((normed_train_data.values, train_labels.values))  # 构建Dataset对象
train_db = train_db.shuffle(100).batch(32)  # 随机打散，批量化


# 自定义网络层，通过继承keras.Model基类
class Network(keras.Model):
    # 分类
    def __init__(self):
        super(Network, self).__init__()
        # 创建3个全连接层
        self.fc1 = keras.layers.Dense(64, activation='relu')
        self.fc2 = keras.layers.Dense(64, activation='relu')
        self.fc3 = keras.layers.Dense(1)

    def call(self, inputs, training=None, mask=None):
        # 依次通过三个全连接层
        x = self.fc1(inputs)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


model = Network()
# 通过 build 函数完成内部张量的创建，其中 4 为任意的 batch 数量，40为输入特征长度
model.build(input_shape=(4,40))
model.summary()  # 打印网络信息
optimizer = tf.keras.optimizers.RMSprop(0.001)  # 创建优化器，指定学习率

# 网络训练部分。通过 Epoch 和 Step 的双层循环训练网络，共训练 200 个 epoch:
for epoch in range(200):  # 200 个 Epoch
    for step, (x, y) in enumerate(train_db):  # 遍历一次训练集
        # 梯度记录器
        with tf.GradientTape() as tape:
            out = model(x)  # 通过网络获得输出
            loss = tf.reduce_mean(keras.losses.MSE(y, out))  # 计算 MSE
            mae_loss = tf.reduce_mean(keras.losses.MAE(y, out))  # 计算 MAE

        if step % 10 == 0:
            print(epoch, step, float(loss))

        # 计算梯度 并更新
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

print()
