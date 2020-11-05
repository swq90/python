while 1:
    try:
        res = 0
        dic = dict(zip(list('ABCDEF'), range(10, 16)))
        num = input()[:1:-1]
        for i in range(len(num)):
            if num[i].isdigit():
                res += 16 ** i * int(num[i])
            else:
                res += 16 ** i * dic[num[i]]
        print(res)
    except:
        break
