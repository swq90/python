首先 利用公网ip，ssh 连接实例，在实例上配置server ，启动  
本地配置 启动 client ，即可连接至实例   
实例作为桥梁，帮助访问**  

现在同一路由器下有两台主机，A可用利用 ssh B的内网ip 访问B  
ssh默认port为22，我们可以 设置端口映射  将一指定的端口数（例33） 和 主机的内部ip和端口形成映射
ssh B的内部ip port 33 访问主机B  


而现在，小区公用一个公网ip，外部主机无法通过ip访问内部的主机  
那么我们可以利用 实例 作为桥梁，因为它是唯一可以利用公网ip访问的  
    
    a作为client 与 实例server 建立通道   
    b 作为client 发送消息给 实例  
    实例则按设定程序 将b的消息转发给a
很像qq


代理和反向代理？

s=socket.socket(socket.AF_INET,socket.Sock-DGRAM)
s.bind()
在客户端绑定端口

  
