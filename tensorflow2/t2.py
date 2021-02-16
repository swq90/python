import os
import tensorflow as tf
from tensorflow import keras

from keras import layers, Sequential, optimizers, losses
import numpy as np
import pandas as pd
from stock.util.basic import basic
import keras
# from tflearn.layers.core import fully_connected
from keras.datasets import mnist
from keras.layers import Input, Dense
from keras.models import Model
import tensorflow as tf
from tensorflow import keras
from stock.sql.data import save_data, read_data
from sklearn.model_selection import train_test_split

start_date = '20170101'
end_date = '20181231'
TEST_SIZE = 0.3
num_classes = 2
CUT = 0.5
raw_dataset = read_data('daily', start_date=start_date, end_date=end_date)
df = basic().pre_data(raw_dataset, label=['close'], pre_days=5)

data = raw_dataset.merge(df[['ts_code', 'trade_date', 'pre_5_close']], on=['ts_code', 'trade_date'])
data['pct'] = data['close'] / data['pre_5_close'] - 1

# 正样本
data_t = data.loc[data['pct'] > CUT][['ts_code', 'trade_date', 'pct']].copy()

# 负样本
data_f = data.loc[data['pct'] < CUT][['ts_code', 'trade_date', 'pct']].copy()
data_f = data_f.sample(n=data_t.shape[0], random_state=1)


def pro(data, label):
    data_sample = np.zeros(shape=(data.shape[0], 40))
    for i in range(data.shape[0]):
        # print(data.iloc[i])
        # df=data.iloc[i,:].copy().sort_values('trade')
        df = raw_dataset.loc[(raw_dataset['ts_code'] == data.iloc[i, 0]) & (
                raw_dataset['trade_date'] < data.iloc[i, 1])].sort_values('trade_date').iloc[-5:]
        if df.shape[0] >= 5:
            df = np.array(df.drop(columns=['ts_code', 'trade_date', 'pre_close'])).reshape(1, -1)
            # df=np.array(np.append(df,np.array(data.iloc[i,-1])))
            data_sample[i] = df

    data_sample = pd.DataFrame(data_sample).dropna()
    data_sample['pct'] = label
    return data_sample


datatest = pd.concat([pro(data_t, 1), pro(data_f, 0)], ignore_index=True)

x, y = datatest.iloc[:, :-1], datatest.iloc[:, -1]

print(x.shape, y.shape)
# 查看x的统计数据？
train_stats = x.describe()
print(train_stats)
train_stats = train_stats.transpose()

print(train_stats)


# 标准化数据
def norm(x):
    return (x - train_stats['mean']) / train_stats['std']


normed_train_data = norm(x)
# normed_test_data = norm(test_dataset)

# print(normed_train_data.shape, train_labels.shape)
# print(normed_test_data.shape, test_labels.shape)

# 利用切分的训练集数据构建数据集对象
X_train, X_test, y_train, y_test = train_test_split(normed_train_data, y, test_size=TEST_SIZE, random_state=42)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

#
# 创建 n 层的全连接层网络
network = Sequential([layers.Dense(10, activation='relu'),
                       layers.Dense(2)])
network.build(input_shape=(None, 40))
network.summary()

# 设置测量指标为准确率,学习率0.01，softmax为损失函数
network.compile(optimizer=optimizers.Adam(lr=0.01), loss=losses.CategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

summary_writer = tf.summary.create_file_writer(os.getcwd())

# 指定训练集为 train_db，验证集为 val_db,训练 200 个 epochs，每 5 个 epoch 验证一次 # 返回训练信息保存在 history 中
history = network.fit(X_train,y_train,
          batch_size=32,
          epochs=10,
          validation_data=(X_test, y_test))
# tf.keras.experimental.export_saved_model(network, 'model-savedmodel')
# print('export saved model.')