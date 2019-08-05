class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.val) == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)
        self.val.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.val):
            if self.val[-1] == self.min[-1]:
                self.min=self.min[:-1]
            self.val=self.val[:-1]

    def top(self):
        """
        :rtype: int
        """
        if len(self.val):
            return self.val[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()