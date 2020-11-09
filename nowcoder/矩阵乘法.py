x,y,z=int(input()),int(input()),int(input())
arr1,arr2=[],[]
for i in range(x):
    arr1.append(list(map(int,input().split())))
for j in range(y):
    arr2.append(list(map(int,input().split())))

for i in range(x):
    res=[]
    for j in range(z):
        s=0
        for k in range(y):
            s+=arr1[i][k]*arr2[k][j]
        res.append(s)
    print(' '.join(map(str,res)))

