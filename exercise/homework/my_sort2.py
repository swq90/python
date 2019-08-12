from  datetime import datetime
def my_sort(l,low,high):
    if low == high:
        return l
    m = low
    for i in range(high):
        if l[i] < l[m] :
            x=l[i]
            l.pop(i)
            l.insert(0,x)
            if m+1==high:
                return l
            else:
                m=m+1

    my_sort(l,0,m)
    my_sort(l,m+1,high)
    return l

def my_sort1(l):
    for i in  range( len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                x=l[i]
                l[i]=l[j]
                l[j]=x
    return (l)

import random
a=100
s=[]
for i in range(100):
    s.append(int(random.random()*a))
s2=s[:]
t1=datetime.now()
my_sort(s,0,len(s))
t2=datetime.now()
print(t2-t1)

my_sort1(s2)
t3=datetime.now()
print(t3-t2)
print(s)




