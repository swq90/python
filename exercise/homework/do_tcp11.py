import socket
#创建socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ipv4,stream,Socket对象创建但是未连接
#建立连接
s.connect(('www.sina.com.cn',80))#每个服务都有标准端口号，网页是80
#发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

       #https://www.runoob.com/http/http-messages.html
#接收数据
buffer = []

while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
#关闭连接
s.close()
#网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)