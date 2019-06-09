class Solution:
    def plusOne(self, digits):
        for i in range(1, len(digits) + 1):
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            digits[-i] = 0
            if i == len(digits):
                digits.insert(0, 1)
                return digits
