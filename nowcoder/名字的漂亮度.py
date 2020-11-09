k=int(input())
for _ in range(k):
    name=input()
    c=[]
    m,res=26,0
    for i in set(name):
        c.append(name.count(i))
    c=sorted(c,reverse=True)
    for i in sorted(c):
        res+=m*i
        m-=1
    print(sum(res))




print(dict)