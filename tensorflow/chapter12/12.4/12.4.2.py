import tensorflow as tf
c = tf.compat.v1.constant ("Hello from server1 !" )
# 生成－个有两个任务的集群，一个任务跑在本地2222端口，另外一个跑在本地 2223 端口 。
cluster = tf.train.ClusterSpec({"local": ["localhost : 2222", "localhost: 2223"]})
# 通过上面生成的集群配置生成 Server，并通过〕ob name 和 task index 指定当前所启动 ＃的任务。肉为该任务是第一个任务，所以 task index 为 0。
server = tf.distribute.Server(cluster, job_name="local", task_index=0)
# 通过 server.target生成会话来使用 TensorFlow 集群中的资源。通过设置 # log device placement 可以看到执行每一个操作的任务。
sess = tf.compat.v1.Session(server.target, config=tf.compat.v1.ConfigProto(log_device_placement=True))
print(sess . run(c))
server . join()