import tensorflow as tf

global_step = tf.compat.v1.Variable(0)
# exponential_decay 生成学习率(learning_rate,global_step,decay_steps,decay_rate,staircase)
learning_rate = tf.train.exponential_decay(0.1, global_step, 100, 0.96, staircase=True)
sess = tf.compat.v1.Session()
sess.run(global_step.initializer)
print(sess.run(global_step))
sess.close()