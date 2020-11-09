
l1,l2=input(),input()
if len(l1)>len(l2):
    l1,l2=l2,l1
x=0
max_len=0
res=''
for i in range(len(l1)):
    if l1[i:i+x] in l2:
        if (x+1)>max_len:
            res=l1[i:i+x]
            max_len=x+1
        x+=1
print(res)
