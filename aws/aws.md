
#####创建实例
    step 1:选择一个amazon系统印象AMI
        Red Hat Enterprise Linux 8 (HVM), SSD Volume Type - ami-09f31cc5d5eecca1a
    step 2：选择一个实例类型
        通用型 t2.micro (变量 ECU, 1 vCPU, 2.5 GHz, Intel Xeon Family, 1 GiB 内存, 仅限于 EBS)
    step 3: 配置实例详细信息
        默认未做更改
    step 4: 添加存储
        默认 根目录：/dev/sda1     修改：30g
    step 5: 添加标签
        默认未做更改
    step 6: 配置安全组
        默认未做更改
            shadowsocksr客户端配置后依然无法访问外网，
        ！设置为 0.0.0.0/0 的源规则允许所有 IP 地址访问您的接口。我们建议将安全组规则设置为仅允许从已知的 IP 地址进行访问。
    step 7: 核查实例启动
        前面设置的所有信息
       
    启动 : 选择现有密钥对或创建新密钥对
        aws2019.pem



#####连接实例
    step 1 :打开ssh客户端
        用git bash here 可以直接执行linux命令
    step 2 ：密钥私有化
        chmod 400 aws2019.pem
    step 3 ： 公用DNS连接到实例     
        ssh -i "aws2019.pem" ec2-user@公用DNS
        ssh -i "aws2019.pem" ec2-user@ip  （ip就是由dns解析出来的）
    可选：安装   AWS CLI
        pip3 install awscli --upgrade --user
        python -m pip install --upgrade pip #更新至最新        
#####ShadowsocksR

######Server
    step 1 :CentOS
        yum install git
        git clone https://github.com/shadowsocksrr/shadowsocksr.git
    step 2 :linux platform
        (move to /shadowsocksr)
        bash init cfg.sh
        (move to /shadowsocksr/shadowsocks)
        python server.py -p 443 -k password -m aes-128-cfb -O auth_aes128_md5 -o tls1.2_ticket_auth_compatible    
        p:端口号；k:密码；m:加密；O:协议；o：混淆
        ./logrun.sh
            = nohub python server.py -p 443 -k password -m aes-128-cfb -O auth_aes128_md5 -o tls1.2_ticket_auth_compatible &
            后台运行，断开连接不中止
    其他命令：
        ./stop.sh
        ./tail.sh   监控日志
    
   
 
######Client
    https://github.com/shadowsocksrr/shadowsocksr-csharp
    配置：
        ShadowsocksR-win-4.9.2.zip
        7-zip
            right-click on the downloaded 7z file and select CRC SHA > SHA-256.
            then:do 7-Zip > Extract Here or extract to a new folder
        
        win8以上用4.0.exe
    使用：
        按server里启动时设置的信息
    
    
    
    
#####Linux语句
    sodu +指令：以root系统管理这执行
    ll,ls
    man 方法名
    rm -rf 删除的文件名或目录
    
    ps -aux|grep python
        显示当前进程process状态，aux显示所有包含使用者的进程，grep分组
    查看文件 
        less -MN logrun.sh
        cat ./logrun.sh
    编辑文件：
        vi 文件名
        esc，shift + : 
        编辑插入 i
        其他命令
    pwd 查看当前目录  
    whoami 用户名
    su - 去root
    
    cd / 回根目录
    cd ~ 回用户主目录
    cd . 当前目录
    cd .. 回到上级目录
    cd 路径
    ifconfig
    查看防火墙状态：
    firewall-cmd --state
    查文件：
    find / -name login*.conf
    在根目录小寻找文件
    iptable
    yum常用命令
1.列出所有可更新的软件清单命令：yum check-update
2.更新所有软件命令：yum update
3.仅安装指定的软件命令：yum install <package_name>
4.仅更新指定的软件命令：yum update <package_name>
5.列出所有可安裝的软件清单命令：yum list
6.删除软件包命令：yum remove <package_name> 
7.查找软件包 命令：yum search <keyword> 
8.清除缓存命令: 
yum clean packages: 清除缓存目录下的软件包
yum clean headers: 清除缓存目录下的 headers
yum clean oldheaders: 清除缓存目录下旧的 headers
yum clean, yum clean all (= yum clean packages; yum clean oldheaders) :清除缓存目录下的软件包及旧的headers
    
    
    
    

#####安装python
    sudo yum install python36

#####无法连接的问题：
    1.重新分配ip
    2.安全组设置，放宽出入站规则
    
[Error] System.Net.Sockets.SocketException (0x80004005): 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。 220.250.64.225:443
   在 System.Net.Sockets.Socket.InternalEndConnect(IAsyncResult asyncResult)
   在 System.Net.Sockets.Socket.EndConnect(IAsyncResult asyncResult)
   在 Shadowsocks.Controller.Socks5Forwarder.Handler.ConnectCallback(IAsyncResult ar)
