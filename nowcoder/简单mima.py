key = list(range(2, 10))
val = [ 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
dic = dict(zip(key, val))
res=''
for c in input():
    if c.islower():
        for i in range(2,10):
            if c in dic[i]:
                res+=str(i)
                break
    elif c.isupper():
        if c=='Z':c='a'
        else:c=chr(ord(c.lower())+1)
        res+=c
    else:
        res+=c
print(res)
