from urllib import request

# with request.urlopen('https://www.python.org') as f:
#     data = f.read()
    # print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():

    #     print('%s: %s' % (k, v))
    # # print('Data:', data.decode('utf-8'))
req = request.Request('http://www.douban.com/')
#add_header 加HTTP头，伪装为浏览器
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
    #返回移动版网页

#Post：如果要以POST发送一个请求，只需要把参数data以bytes形式传入
#post是啥



