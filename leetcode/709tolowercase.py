class Solution:
    def toLowerCase1( str: str) -> str:
        return str.lower()

    def toLowerCase2( str: str) -> str:
        res = ''
        t = [ord(x) for x in str]
        for i in range(len(str)):
            if t[i]>=65 and t[i] <= 90:
                str = str.replace(str[i],chr(t[i]+32))
        return str

