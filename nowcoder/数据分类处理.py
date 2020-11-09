I,R=list(input().split())[1:],list(set(list(map(int,input().split()))[1:]))
R.sort()
R=list(map(str,R))
res=[]
for i in range(len(R)):
    s=[]
    for j in range(len(I)):
        if R[i] in I[j]:
            s.append(str(j))
            s.append(I[j])
    if s:
        res.append(R[i])
        res.append(str(len(s)//2))
        res+=s
print(str(len(res))+' '+' '.join(res))
