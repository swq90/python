def f(n):
    if n<=2:
        sum=1
    else:
        sum=f(n-1)+f(n-2)
    return sum
# print(f(3))
# print(f(4))
# print(f(5))
# print(f(6))
# print(f(7))


dtuzi = 0
xtuzi = 1
for i in range(2,13):
    print(i)
    temp = dtuzi
    dtuzi = xtuzi+temp
    xtuzi = temp
    total = dtuzi + xtuzi;
print(total)