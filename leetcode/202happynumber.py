# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number
# by the sum of the squares of its digits, and repeat the process
# until the number equals 1 (where it will stay),
# or**** it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
def isHappy(n):
    result = n
    l = [n, ] #记录sum，判断是否进入循环
    while result != 1:
        s = 0

        while result != 0:
            x = result % 10
            sum += x ** 2
            result = result // 10
        if s in l:
            return False
        else:
            result = s
            l.append(result)
    return True