while True:
    try:
        keys, origin = input().upper(), input()
        code, res = [], ''
        for i in keys:
            if i not in code:
                code.append(i)
        for i in range(65, 91):
            if chr(i) not in code:
                code.append(chr(i))
        for i in origin:
            if i not in code:
                res += chr(ord(code[ord(i) - 97]) + 32)
            else:
                res += (chr(code[ord(i) - 65]))
        print(res)
    except:
        break
