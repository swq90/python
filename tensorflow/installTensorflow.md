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