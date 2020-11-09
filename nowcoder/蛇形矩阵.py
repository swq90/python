while True:
    try:


        n, curNum = int(input()), 1
        res = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i + 1):
                res[i - j][j] = curNum
                curNum += 1
        for i in res:
            print(" ".join(map(str, (filter(lambda i: i != 0, i)))))


    except:
        break
