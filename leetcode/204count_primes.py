class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0
        # if n >2:
        r = 1
        for i in range(3,n,2):
            j = 3
            # print(i)
            while j*j < i:
                if i%j == 0:
                    break
                j += 2
            if i <= j*j:
                r += 1
        return r
#
# 1.求质数，满足条件count+1
# 2.超时，如何改进？
# 想到从2开始，所有2的倍数可以忽略，有了line12。
# 判断质数时可以不用遍历到要判断的数，因为分解后的因式在后半段只需要交换顺序即可。
# line19原来判断i<=j,改进后=要去掉，3*3=9
# 3.依然超时，此时是n**1.5
# 4.hint提示Sieve of Eratosthenes，再以前做题有过这个思路，但是不会写
    # 下面的方法实现了上面的方法，list可以这样操作，要学习

    def countPrimes2(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


# 方法2，discuss里第一的答案