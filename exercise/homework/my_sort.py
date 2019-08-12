def my_sort(l):
    for i in  range( len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                x=l[i]
                l[i]=l[j]
                l[j]=x
    return (l)
#
# l=[7,6,5,4,3,2,9]
# l.pop(2)
# print(l)
# s1=l[int(len(l)/2):]
# print(s1)
# print(my_sort(l))
# print(int(len(l)/2))
