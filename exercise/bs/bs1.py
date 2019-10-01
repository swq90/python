# coding=UTF-8
import pydevd
from wsgiref.simple_server import make_server


def application(environ, start_response):
    # charset=UTF-8，几个encode有什么不同
    #
    start_response('200 OK', [('Content-Type', 'text/html;charset=UTF-8')])
    body = ""
    with open("plan.txt", 'r', encoding='ANSI') as f:
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
