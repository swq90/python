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
            elif i == '/':
                temp.append(int(temp.pop(-2) / temp.pop()))
            else:
                temp.append(int(i))
        return  temp.pop()

# leetcode提交结果与本地结果不同？
