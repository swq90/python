#求正整数的补数，正整数的二进制按位翻转
#解题，第一反应异或，二进制位长度问题学习到新函数bit_length

class Solution:

    def findComplement(self, num: int) :

        return  num^(2**num.bit_length()-1)



o=Solution()
print(o.findComplement(50))