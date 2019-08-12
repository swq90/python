db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
import hashlib
#根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    pw=hashlib.md5()
    pw.update(password.encode('utf_8'))
    return pw.hexdigest()

def login(user, password):
    if calc_md5(password)==db[user]:    #dict[user]
        return True
    else:
        return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')