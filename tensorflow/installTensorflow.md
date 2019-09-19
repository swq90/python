# 安装tensorflow
    https://tensorflow.google.cn/install/pip
##1.在系统上安装python
    1：install python3,pip3,virtualenv,检查版本
    2：确保启用长路径https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing
        i:win10家庭版没有策略组:创建文件 策略组.cmd
        ii:Local Computer PolicyComputer ConfigurationAdministrative TemplatesSystemFilesystemNTFS
            Enable NTFS long paths
##2.创建虚拟环境
###创建
    D:\workgit\>virtualenv --system-site-packages -p python3 ./venv
        报错：The path python3 (from --python=python3) does not exist
    --system-site-packages，默认虚拟环境中不包括系统的site-packages,若需要则要自行添加
        让虚拟环境继承系统的安装包 
        pip list，可以看出二者的区别
    -p python3,指定python的解释器版本，系统中只安装一个版本，则默认为该版本
    
    D:\workgit>virtualenv --system-site-packages  ./venv        成功
    virtualenv -h，查看帮助
    
    多个虚拟环境管理？
###激活
激活：D:\workgit\venv\Scripts>activate
退出：deactivate
##安装tensorflow 
    pip install --upgrade tensorflow
    python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    
版本    
'1.14.0'
路径
['D:\\workgit\\venv\\lib\\site-packages\\tensorflow\\python\\keras\\api\\_v1', 'c:\\users\\wqsha\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\tensorflow_estimator\\python\\estimator\\api\\_v1', 'D:\\workgit\\venv\\lib\\site-packages\\tensorflow', 'D:\\workgit\\venv\\lib\\site-packages\\tensorflow\\_api\\v1']
>>>


##linux上安装TensorFlow

虚拟环境：

    pip install virtualenv
    virtualenv ENV
    source ENV/bin/activate
    
# TensorFlow主要依赖包
##Protocol Buffer
处理结构化数据的工具（拥有多种属性的数据）
比如用户信息中包含名字、ID和E-mail地址三种不同属性，那么它就是一个结构化数据。要将这些结构化的用户信息持久化或者进行网络传输时，就需要先将它们序列化。
所谓序列化，是将结构化的数据变成数据流的格式，简单地说就是变为一个字符串。将结构化的数据序列化，井从序列化之后的数据流中还原出原来的结构化数据，统称为处理结构化数据，这就是Protocol Buffer解决的主要问题。
除Protocol Buffer之外，XML和JSON是两种比较常用的结构化数据处理工
Protocol Buffer 格式的数据和 XML 或者 JSON 格式的数据有比较大的区别。
    Protocol Buffer 序列化之后得到的数据不是可读的字符串，而是二进制流
    XML 或 JSON 格式的数据信息都包含在了序列化之后的数据中，不需要任何其他信息就能还原序列化之后的数据。但使用 Protocol Buffer 时需要先定义数据的格式（schema）还原一个序列化之后的数据将需要使用到这个定义好的数据格式。 
Protocol Buffer 定义数据格式的文件一般保存在.proto文件中
message 里面定义了每一个属性的类型和名字。 Protocol Buffer 里属性的类型可以是像布尔型、整数型、实数型、字符型这样的基本类型，也可以是另外一个message
也定义了一个属性是必需的required还是可选的optional，或者是可重复的repeated
分布式 TensorFlow 的通信协议 gRPC 也是以 Protocol Buffer 作为基础的。

```xml
<user>
    <name>tom</name>
    <id>12345</id>
    <email>tom@abc.com</email>
</user>
```
```json
{
  "name": "tom",
  "id": "12345",
  "email": "tom@abc.com"
}
```
```
message user{
    optional string name = 1;
    required int32 id = 2;
    repeated string email = 3;

}
```
## Bazel
Bazel是从谷歌开源的自动化构建工具，谷歌内部绝大部分的应用都是通过它来编译的
项目空间（workspace）是 Bazel 的一个基本概念。一个项目空间可以简单地理解为一个文件夹，在这个文件夹中包含了编译一个软件所需要的源代码以及输出编译结果的软连接（symbolic link）地址。
项目空间所对应的文件夹是这个项目的根目录，在这个根目录中需要有一个 WORKSPACE 文件，此文件定义了对外部资源的依赖关系。空文件同样也是一个合法的WORKSPACE文件
在一个项目空间内， Bazel 通过 BUILD 文件来找到需要编译的目标。BUILD 文件采用一种类似于 Python 的语法来指定每一个编译目标的输入、输出以及编译方式
    Bazel 对 Python 支持的编译方式只有三种：py_binary,py_library,py_test
        py_binary 将 Python 程序编译为可执行文件
        py_test编译 Python 测试程序
        py_library 将 Python 程序编译成库函数供其他py_binary可 或 PY一test 调用
BUILD 文件是由一系列编译目标组成的。定义编译目标的先后顺序不会影响编译的结果。在每一个编译目标的第一行要指定编译方式，


Intel(R) UHD Graphics 620
NVIDIA GeForce MX130



