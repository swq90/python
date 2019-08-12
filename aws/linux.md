##centos7安装pip
1.安装
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py


安装python3.7
1、下载
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
2、解压 
tar  -xf    ***.tgz
3、编译
./configure && make && make install

配置yum源和epel源
    
    进入存放yum源配置的文件夹
    [nezha@bogon yum.repos.d]$ cd /etc/yum.repos.d
    备份
    [nezha@bogon yum.repos.d]$ sudo mv ./CentOS-Base.repo ./CentOS-Base.repo.bak
    阿里和163开源镜像下载对应版本的repo文件
    wget http://mirrors.aliyun.com/repo/Centos-7.repo
    wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
    ls
        Centos-7.repo  CentOS-Base-163.repo
    清除yum缓存，
    yum clean all
    生成新的缓存
    yum makecache
    安装epel源
    yum list | grep epel-release#啥意思
    yum install -y epel-release
    ls查看，发现多了epel.repo  and epeltesting.repo
    使用阿里开源的epel源
    wget -O /etc/yum.repos.d/epel-7.repo http://mirrors.aliyun.com/repo/epel-7.repo 
    ls查看，多了epel-7.repo
    清缓存，生成新的缓存
    yum clean all
    yum makecache
    
    查看可用yum源和所有yum源
    yum repolist enabled
    yum repolist all
    

安装python
安装pip
    Successfully installed pip-19.2.1 setuptools-41.0.1 wheel-0.33.4   
    
##其他
 netstat -anp |grep 443  
 ps -aux|grep 443  
 ps -aux|grep sserver  
 
 [ec2-user@ip-172-31-36-225 ~]$ netstat -anp |grep 443
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 172.31.36.225:54433     74.125.203.188:5228     ESTABLISHED -
tcp        0      0 172.31.36.225:40763     52.114.74.43:443        TIME_WAIT   -
tcp6       0      0 :::443                  :::*                    LISTEN      -
tcp6       0      0 172.31.36.225:443       122.96.9.52:58921       TIME_WAIT   -
tcp6       0      0 172.31.36.225:443       122.96.9.52:58917       TIME_WAIT   -
tcp6       0      0 172.31.36.225:443       122.96.9.52:58928       ESTABLISHED -
udp        0      0 0.0.0.0:34432           0.0.0.0:*                           -
udp6       0      0 :::443                  :::*                                -
unix  3      [ ]         STREAM     CONNECTED     901443   -

传输文件
scp ./aws2019.pem root@10.0.0.10:/tmp
root@10.0.0.10's password:
aws2019.pem                                   100% 1692   164.5KB/s   00:00

kill -9