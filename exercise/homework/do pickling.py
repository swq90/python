import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)#把任意对象序列化成bytes，然后将bytes写入文件
f=open(r'C:\Users\wqsha\Desktop\test3.txt', 'wb')
pickle.dump(d,f)
f.close()

with open(r'C:\Users\wqsha\Desktop\test3.txt','rb') as f:
    print(f.read())

#要把对象从磁盘读入内存，先读入bytes，然后用pickle.loads()反序列化出对象
#或者用pickle.load()从 file like objecet 反序列化处对象
f=open(r'C:\Users\wqsha\Desktop\test3.txt', 'rb')
d = pickle.load(f)
f.close()
print ('反序列化',d)

import json
print(json.dumps(d))
jsonstr='{"name": "Bob", "age": 20, "score": 88}'
print(jsonstr)
print(json.loads(jsonstr))




