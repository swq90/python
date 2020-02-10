import tensorflow as tf
from tensorflow import keras
from keras import layers, Sequential, optimizers, losses

# 首先通过 compile 函数指定网络使用的优化器对象，损失函数，评价指标等：
# 导入优化器，损失函数模块
# 采用 Adam 优化器，学习率为 0.01;采用交叉熵损失函数，包含 Softmax
# 创建 5 层的全连接层网络
network = Sequential([layers.Dense(256, activation='relu'),
                      layers.Dense(128, activation='relu'), layers.Dense(64, activation='relu'),
                      layers.Dense(32, activation='relu'), layers.Dense(10)])
network.build(input_shape=(None, 28 * 28))
network.summary()
network.compile(optimizer=optimizers.Adam(lr=0.01), loss=losses.CategoricalCrossentropy(from_logits=True),
                metrics=['accuracy']  # 设置测量指标为准确率
                )
# 8.2.2模型训练
# 模型装配完成后，即可通过 fit()函数送入待训练的数据和验证用的数据集
# 指定训练集为 train_db，验证集为 val_db,训练 5 个 epochs，每 2 个 epoch 验证一次
# 返回训练信息保存在 history 中
history = network.fit(train_db, epochs=5, validation_data=val_db, validation_freq=2)
# 其中 train_db 为 tf.data.Dataset 对象，也可以传入 Numpy Array 类型的数据；epochs 指定训 练迭代的 epochs 数；validation_data 指定用于验证(测试)的数据集和验证的频率 validation_freq。 运行上述代码即可实现网络的训练与验证的功能，fit 函数会返回训练过程的数据记录 history，其中 history.history 为字典对象，包含了训练过程中的 loss，测量指标等记录项：
history.history # 打印训练记录

# 加载一个 batch 的测试数据
x,y = next(iter(db_test))
print('predict x:', x.shape)
out = network.predict(x) # 模型预测
print(out)
network.evaluate(db_test)#模型测试

#8.3.1
network.save_weights('weights.ckpt')
print('saved weights')
del network
# 重建相同网络结构
network = Sequential([layers.Dense(256, activation='relu'),
                      layers.Dense(128, activation='relu'), layers.Dense(64, activation='relu'),
                      layers.Dense(32, activation='relu'), layers.Dense(10)])

network.compile(optimizer=optimizers.Adam(lr=0.01), loss=losses.CategoricalCrossentropy(from_logits=True),
                metrics=['accuracy']  # 设置测量指标为准确率
                )
# 从参数文件中读取数据并写入当前网络
network.load_weights('weights.ckpt')
print('loaded weights')