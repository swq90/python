n = int(input())
num = 0
for i in range(n + 1):
    n2 = str(i ** 2)
    i=str(i)
    if i == n2[-len(i):]:
        num += 1
print(num)