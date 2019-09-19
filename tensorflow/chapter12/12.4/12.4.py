import tensorflow as tf

c = tf.compat.v1.constant("hello,distributed tensorflow")
server = tf.compat.v1.train.Server.create_local_server()
sess = tf.compat.v1.Session(server.target)
print(sess.run(c))