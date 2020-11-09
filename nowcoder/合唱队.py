def left(l):
    res=[1]*len(l)
    for i in range(len(l)):
        for j in range(i):
            if l[j]<l[i] and res[j]+1>res[i]:
                res[i]=res[j]+1
    return res
def right(l):
    res=[1]*len(l)
    for i in range(len(l)-1,-1,-1):
        for j in range(i+1,len(l)):
            print(l[i],l[j])
            if l[i]>l[j] and res[j]+1>res[i]:
                res[i]=res[j]+1
    return res

N=int(input())
line=list(map(int,input().split()))
res=max(map(lambda x,y:x+y,left(line),right(line)))
print(N-res+1)


