import tensorflow as tf

global_step = tf.compat.v1.Variable(0)
# exponential_decay 生成学习率(learning_rate,global_step,decay_steps,decay_rate,staircase)
learning_rate = tf.train.exponential_decay(0.1, global_step, 100, 0.96, staircase=True)

# 指数衰减学习率，在minimize函数中掺入global_step将自动更新global——step参数，是的学习率得到更新
# learning_step = tf.train.GradientDescentOptimizer()

# 学习率0.1，训练100轮后学习率乘以0.96，