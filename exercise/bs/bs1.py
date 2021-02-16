# coding=UTF-8
import pydevd
from wsgiref.simple_server import make_server


def application(environ, start_response):
    # environ：一个包含所有HTTP请求信息的dict对象；
    # start_response：一个发送HTTP响应的函数。
    # charset=UTF-8，几个encode有什么不同

    start_response('200 OK', [('Content-Type', 'text/html;charset=UTF-8')])
    # Header只能发送一次，start_response只能调用一次,参数1，HTTP响应码，参数2，当前内容的MIME类型
    # Content-Type指定了body的类型，charset=utf-8规定了外务文件中使用的字符编码，如果外部文件字符编码与主文件编码不同，会用到charset


    #读取非utf-8编码的文件要传encoding参数，将字符串转换成指定编码
    body = ""
    with open("plan.txt", 'r', encoding='UTF-8') as f:
        contents = f.readlines()
        for content in contents:
            body += '<h1>' + content+'</h1>'
    return [body.encode()]


# 创建一个服务器，IP地址为空，端口是8088，处理函数是application:
httpd = make_server('', 8088, application)
print('Serving HTTP on p'
      't 888...')
# 开始监听HTTP请求:
httpd.serve_forever()
