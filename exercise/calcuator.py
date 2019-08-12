class Calcuator(object):
    operator = {'+': 1, '-': 2, '*': 3, '/': 4, '(': 5, ')': 6}
    o = []

    def strtonums(s):

        nums = []
        t = ''
        for i in range(len(s)):
            if s[i] in Calcuator.operator:
                if t :
                    nums.append(float(t))
                nums.append(s[i])

                t = ''
            else:
                t += s[i]
        if t:
            nums.append(float(t))
        return nums
    def operation(nums):
        if len(nums) == 1:
            return nums[0]

        i =0
        while i < len(nums):
            if nums[i] == "*" :
                nums[i-1] = nums[i-1]*nums[i+1]
                nums.pop(i)
                nums.pop(i)
            elif nums[i] == "/" :
                nums[i-1] = nums[i-1]/nums[i+1]
                nums.pop(i)
                nums.pop(i)
            else:
                i += 1
        i = 0
        while i < len(nums):
            if nums[i] == "+" :
                nums[i-1] = nums[i-1]+nums[i+1]
                nums.pop(i)
                nums.pop(i)
            elif nums[i] == "-" :
                nums[i-1] = nums[i-1]-nums[i+1]
                nums.pop(i)
                nums.pop(i)
            else:
                i += 1
        return nums

    def delbrackets (nums):
        brackets = []#记录左括号
        i = 0
        while i < len(nums):
            if nums[i] == '(':
                brackets.append(i)
            elif nums[i] == ')':
                nums[brackets[-1]:i+1]=Calcuator.operation(nums[brackets[-1]+1:i])
                i = brackets[-1]
                brackets.pop()
            i += 1




    def run(self,s):
        nums = Calcuator.strtonums(s)

        print(nums)
        Calcuator.delbrackets(nums)
        res=Calcuator.operation(nums)
        print(res)


o=Calcuator()
o.run('((3*8*(1+2)+3)/5/3+2-(3+1))')