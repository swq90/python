class Solution:
    # ax + by +cz = amount;
    def change(self, amount: int, coins: [int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for j in coins:
            for i in range(1, amount + 1):
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[amount]


def f(month: int) -> int:
    # 0,1,1,2,3,5,8,13,21
    dp = []*month
    dp[0] = 0
    dp[1] = 1
    for i in range(2, month):
        dp[i] = dp[i - 1] + dp[i - 2]


def f2(month):
    if month == 1:
        return 1
    if month == 0:
        return 0
    return f2(month - 1) + f2(month - 2)


# 0,1,1,2,3,5,8,13,21

def f3(n, pre, now):
    if n == 0:
        return pre
    if n == 1:
        return now
    return f3(n - 1, now, pre + now)


print(f2(10))
print(f3(10, 0, 1))
