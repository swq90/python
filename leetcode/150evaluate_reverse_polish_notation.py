class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        temp =[]

        for i in tokens:
            if i == '+':
                temp.append(temp.pop()+temp.pop())

            elif i == '-':
                temp.append(temp.pop(-2) - temp.pop())
            elif i == '*':
                temp.append(temp.pop() * temp.pop())
            # elif i == '/':
            #     temp.append(int(temp.pop(-2) / temp.pop()))
            elif i == '/':
                m, n = temp.pop(-2), temp.pop()
                if m / n < 0 and m % n != 0:
                    temp.append(int(m / n) + 1)
                else:
                    temp.append(int(m / n))
            else:
                temp.append(int(i))
        return temp.pop()


# leetcode提交结果与本地结果不同？
# leetcode 开始选择了python而不是python3，int 向下取整