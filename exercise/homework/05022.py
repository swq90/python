def han(n,x,y,z):
    if n==1:
        print('move','1', 'from', x, 'to', z)
    else:
        han(n - 1, x, z, y)
        print('move', n, 'from', x, 'to', z)
        han(n - 1, y ,x, z)

print('========')
han(3,'a','b','c')
