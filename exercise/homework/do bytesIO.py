from io import BytesIO
f=BytesIO('邵文琴'.encode('utf8'))#-,下划线，空格均可
print(f.getvalue())
#可以用bytes初始化一个
f=BytesIO(b'\xe9\x82\xb5\xe6\x96\x87\xe7\x90\xb4')
print(f.getvalue())
