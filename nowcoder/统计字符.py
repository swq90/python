while 1:
    try:
        line = input()
        res = [0] * 4
        for i in line:
            if i.isalpha():
                res[0] += 1
            elif i == ' ':
                res[1] += 1
            elif i.isdigit():
                res[2] += 1
            else:
                res[3] += 1
        for i in res:
            print(i)
    except:
        break
