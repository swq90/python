class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = []
        count = 0
        for i in range(len(T)):
            j = i + 1
            while j<len(T):
                if T[i]<T[j]:
                    res.append(j-i)
                    count += 1
                    break
                j += 1
            if count < i+1:
                res.append(0)
                count += 1
        return res

def dailyTemperatures2(self, T):
        res, stack = [0]*len(T), []
        for i in range(len(T)):

            while stack and T[stack[-1]] < T[i]:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
        return res

# line26，while
