class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        d =["+","-"," "]
        n = 0
        sign = 1
        condition = 1
        for i in str:
            if ord(i) < 48 or ord(i) > 57:
                if i in d:
                    continue
                else:
                    return n
            if condition:
                if i == " ":
                    break
                elif i == "+":
                    condition = 0
                elif i == "-":
                    sign = -1
                    condition = 0

        # sign = [1, ]
        # n = 0
        # for i in str:
        #     if len(sign) > 2:
        #         return 0
        #     if i == " ":
        #         continue
        #     elif i == "-":
        #         sign.append(-1)
        #     elif i == "+":
        #         sign.append(1)
        #
        #     elif ord(i) >= 48 and ord(i) <= 57:
        #         n = n * 10 + ord(i) - 48
        #         if n > pow(2, 31) - 1:
        #             if sign == 1:
        #                 return pow(2, 31) - 1
        #             else:
        #                 return -pow(2, 31)
        #     else:
        #         break
        # return sign * n