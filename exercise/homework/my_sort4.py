from datetime import datetime
import random
def my_sort4(l):
    if len(l)!=1 :
        base = l[0]
        i=0
        j=len(l)-1
        while i < j :
            while (i < j) and (l[j] >= base):
                j=j-1
            while (i < j) and (l[i] <= base):
                i=i+1
            if i < j :
                t=l[i]
                l[i]=l[j]
                l[j]=t
        l[0]=l[i]
        l[i]=base
        if(i!=0) :
            my_sort4(l[:i-1])
        if(i<len(l)-1):
            my_sort4(l[i+1:])


a=10000
s=[]
for i in range(5000):
    s.append(int(random.random()*a))
print(s)
s1=s[:]
# t1=datetime.now()
my_sort4(s)
print(s)
