from datetime import datetime
import random
def my_sort3(l,low,high):
    if low < high :
        base = l[low]
        i=low
        j=high
        while i < j :
            while (i < j) and (l[j] >= base):
                j=j-1
            while (i < j) and (l[i] <= base):
                i=i+1
            if i < j :
                t=l[i]
                l[i]=l[j]
                l[j]=t
        l[low]=l[i]
        l[i]=base
        my_sort3(l,low,i-1)
        my_sort3(l,i+1,high)

def my_sort(l):
    for i in  range( len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                x=l[i]
                l[i]=l[j]
                l[j]=x
    return (l)
a=10000
s=[]
for i in range(10000):
    s.append(int(random.random()*a))
s1=s[:]
s2=s[:]
t1=datetime.now()
my_sort3(s,0,len(s)-1)
t2=datetime.now()
# my_sort(s1)
s1.sort()
t3=datetime.now()

print(t2 - t1)
print(t3 - t2)
print(s1==s)
