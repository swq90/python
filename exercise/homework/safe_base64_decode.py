#请写一个能处理去掉=的base64解码函数
import base64
def safe_base64_decode(s):
    a = len(s)%4
    s = s+a*b'='
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')