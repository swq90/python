class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = 0
        p, q = 0, 1
        while q < len(s):
            if s[q] in s[p:q]:
                i = s[p:q].index(s[q])
                length = max(length, q-p)
                p += i + 1
            q += 1
        return max(length, q-p)

# line 15：i相对位置，所以+=
# line 17：开始用q-p+1,忽略了循环退出时q的值
# 要细心啊