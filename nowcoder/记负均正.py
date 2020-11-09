
N = int(input())
nums = []
for j in range(N):
    nums.append(int(input()))
x,y=0,0
for i in nums:
    if i<0:
        x+=1
    else:
        y+=i

print(str(x) + ' ' + '%.1f' % (y/(N-x)) ) if x<N else print('0 0.0')

