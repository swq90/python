while 1:
    try:
        m = int(input())
        res = dict.fromkeys(list(range(m)), 0)
        for i in range(m):
            k, v = map(int, input().split(' '))
            res[k] += v

        for k, v in res.items():
            if v:
                print(k, v)
    except:
        break
