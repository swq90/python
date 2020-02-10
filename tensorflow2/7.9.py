import numpy as np

import sklearn
from sklearn import datasets, model_selection
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# 数据集
N_SAMPLES = 2000  # 采样点数
TEST_SIZE = 0.3  # 测试数量比率
# 利用工具函数直接生成数据集
X, y = datasets.make_moons(n_samples=N_SAMPLES, noise=0.2, random_state=100)
# 将 2000 个点按着 7:3 分割为训练集和测试集
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=TEST_SIZE, random_state=42)
print(X.shape, y.shape)


# 绘制数据集的分布，X 为 2D 坐标，y 为数据点的标签
def make_plot(X, y, plot_name, file_name=None, XX=None, YY=None, preds=None, dark=False):
    if (dark):
        plt.style.use('dark_background')
    else:
        sns.set_style("whitegrid")
    plt.figure(figsize=(16, 12))
    axes = plt.gca()
    axes.set(xlabel="$x_1$", ylabel="$x_2$")
    plt.title(plot_name, fontsize=30)
    plt.subplots_adjust(left=0.20)
    plt.subplots_adjust(right=0.80)
    if (XX is not None and YY is not None and preds is not None):
        plt.contourf(XX, YY, preds.reshape(XX.shape), 25, alpha=1, cmap=sklearn.cm.Spectral)
        plt.contour(XX, YY, preds.reshape(XX.shape), levels=[.5], cmap="Greys", vmin=0, vmax=.6)
    # 绘制散点图，根据标签区分颜色
    plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=40, cmap=plt.cm.Spectral, edgecolors='none')
    plt.savefig('dataset.svg')
    plt.close()


# 调用 make_plot 函数绘制数据的分布，其中 X 为 2D 坐标，y 为标签
make_plot(X, y, "Classification Dataset Visualization ")
plt.show()


# 7.9.2网络层
class Layer:
    # 全连接网络层     
    def __init__(self, n_input, n_neurons, activation=None, weights=None, bias=None):
        """
        :param
        int
        n_input: 输入节点数:param
        int
        n_neurons: 输出节点数:param
        str
        activation: 激活函数类型:param
        weights: 权值张量，默认类内部生成: param
        bias: 偏置，默认类内部生成
        """
        # 通过正态分布初始化网络权值，初始化非常重要，不合适的初始化将导致网络不收敛         
        self.weights = weights if weights is not None else np.random.randn(n_input, n_neurons) * np.sqrt(1 / n_neurons)
        self.bias = bias if bias is not None else np.random.rand(n_neurons) * 0.1
        self.activation = activation  # 激活函数类型，如’sigmoid’
        self.last_activation = None  # 激活函数的输出值 o
        self.error = None  # 用于计算当前层的 delta 变量的中间变量
        self.delta = None  # 记录当前层的 delta 变量，用于计算梯度 

    # 实现网络层的前向传播如下：
    def activate(self, x):
        # 前向传播         
        r = np.dot(x, self.weights) + self.bias  # X@W+b 
        # 通过激活函数，得到全连接层的输出 o        
        self.last_activation = self._apply_activation(r)
        return self.last_activation
        # 其中 self._apply_activation 实现了不同的激活函数的前向计算过程：

    def _apply_activation(self, r):
        # 计算激活函数的输出         
        if self.activation is None:
            return r  # 无激活函数，直接返回
            # ReLU 激活函数         
        elif self.activation == 'relu':
            return np.maximum(r, 0)
            # tanh
        elif self.activation == 'tanh':
            return np.tanh(r)  # sigmoid
        elif self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-r))

        return r

    # 针对于不同的激活函数，它们的导数计算实现如下：
    def apply_activation_derivative(self, r):
        # 计算激活函数的导数
        # 无激活函数，导数为 1
        if self.activation is None:
            return np.ones_like(r)
        # ReLU 函数的导数实现
        elif self.activation == 'relu':
            grad = np.array(r, copy=True)
            grad[r > 0] = 1.
            grad[r <= 0] = 0.
            return grad
        # tanh 函数的导数实现
        elif self.activation == 'tanh':
            return 1 - r ** 2
        # Sigmoid 函数的导数实现
        elif self.activation == 'sigmoid':
            return r * (1 - r)

        return r
    # 可以看到，Sigmoid 函数的导数实现为𝑟 ∗ (1 − 𝑟)，其中𝑟即为𝜎(𝑧)。


# 7.9.3 网络模型
# 实现单层网络类后，我们实现网络模型的类 NeuralNetwork，它内部维护各层的网络层 Layer 类对象，可以通过 add_layer 函数追加网络层，实现如下：
class NeuralNetwork:
    # 神经网络大类
    def __init__(self):
        self._layers = []  # 网络层对象列表 

    def add_layer(self, layer):
        # 追加网络层 
        self._layers.append(layer)

    # 网络的前向传播只需要循环调用个网络层对象的前向计算函数即可：
    def feed_forward(self, X):
        # 前向传播
        for layer in self._layers:
            # 依次通过各个网络层
            X = layer.activate(X)
        return X


# 实例化网络对象，添加4层全连接层：
nn = NeuralNetwork()  # 实例化网络类
nn.add_layer(Layer(2, 25, 'sigmoid'))  # 隐藏层 1, 2=>25
nn.add_layer(Layer(25, 50, 'sigmoid'))  # 隐藏层 2, 25=>50
nn.add_layer(Layer(50, 25, 'sigmoid'))  # 隐藏层 3, 50=>25
nn.add_layer(Layer(25, 2, 'sigmoid'))  # 输出层, 25=>2 


# 网络模型的反向传播实现稍复杂，需要从最末层开始，计算每层的𝛿变量，根据我们推导的梯度公式，将计算出的𝛿变量存储在Layer类的delta变量中。

def backpropagation(self, X, y, learning_rate):
    # 反向传播算法实现
    # 前向计算，得到输出值
    output = self.feed_forward(X)
    for i in reversed(range(len(self._layers))):  # 反向循环
        layer = self._layers[i]  # 得到当前层对象
        # 如果是输出层
        if layer == self._layers[-1]:  # 对于输出层
            layer.error = y - output  # 计算 2 分类任务的均方差的导数
            # 关键步骤：计算最后一层的 delta，参考输出层的梯度公式
            layer.delta = layer.error * layer.apply_activation_derivative(output)
        else:  # 如果是隐藏层
            next_layer = self._layers[i + 1]  # 得到下一层对象
            layer.error = np.dot(next_layer.weights, next_layer.delta)
            # 关键步骤：计算隐藏层的 delta，参考隐藏层的梯度公式
            layer.delta = layer.error * layer.apply_activation_derivative(layer.last_activation)

        # 在反向计算完每层的𝛿变量后，只需要按着 𝜕ℒ 𝜕𝑤𝑖= 𝑜𝑖𝛿公式计算每层的梯度，并更新网络参数即可。由于代码中的delta计算的是−𝛿，因此更新时使用了加号。
        # 循环更新权值
    for i in range(len(self._layers)):
        layer = self._layers[i]
        # o_i 为上一网络层的输出
        o_i = np.atleast_2d(X if i == 0 else self._layers[i - 1].last_activation)
        # 梯度下降算法，delta 是公式中的负数，故这里用加号
        layer.weights += layer.delta * o_i.T * learning_rate

    # 因此，在backpropagation函数中，反向计算每层的𝛿变量，并根据梯度公式计算每层参数的梯度值，按着梯度下降算法完成一次参数的更新。

    # 7.9.4网络训练我们的二分类任务网络设计为2输出节点，因此需要将真实标签y进行one - hot编码：

def train(self, X_train, X_test, y_train, y_test, learning_rate,
          max_epochs):
    # 网络训练函数
    # one-hot 编码
    y_onehot = np.zeros((y_train.shape[0], 2))
    y_onehot[np.arange(y_train.shape[0]), y_train] = 1

# 将one - hot编码后的真实标签与网络的输出计算均方差，并调用反向传播函数更新网络参数，循环迭代训练集1000遍：
    mses = []
    for i in range(        max_epochs):  # 训练 1000 个 epoch
        for j in range(len(X_train)):  # 一次训练一个样本
            self.backpropagation(X_train[j], y_onehot[j], learning_rate)
        if i % 10 == 0:
            # 打印出 MSE Loss
            mse = np.mean(np.square(y_onehot - self.feed_forward(X_train)))
            mses.append(mse)
            print('Epoch: #%s, MSE: %f' % (i, float(mse)))

            # 统计并打印准确率                 '
            print('Accuracy: %.2f%%' % (self.accuracy(self.predict(X_test), y_test.flatten()) * 100))

    return mses

    print()
