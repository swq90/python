while True:
    try:
        total=int(input())
        line=input()
        song=list(range(1,total+1))
        m=0
        s=4
        for i in line:
            m= m-1 if i=='U' or i=='u' else m+1
        z= m%total
        if total<=s:
            print(' '.join(map(str,song)))
        else:
            if m<0:
                if z+s<total:
                    print(' '.join(map(str, song[z-s+1:z+1])))
                else:
                    print(' '.join(map(str, song[-s:])))
            else:
                if z<s:
                    print(' '.join(map(str, song[:s])))
                else:print(' '.join(map(str, song[z:z+s])))
        print(song[z])
    except:
        break
