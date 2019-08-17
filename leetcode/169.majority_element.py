class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = set(nums)
        c = len(nums)/2
        for n in l:
            count = 0
            for x in nums:
                if n == x:
                    count += 1
            if count > c:
                return n


    def majorityElement2(self, nums):
        return sorted(nums)[len(nums)/2]

    def majorityElement3(self, nums):
        major = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == major:
                count += 1
            elif count == 0:
                major = nums[i]
                count +=1
            else:
                count -= 1
        return major


# 1.自己的笨方法
# 2.小聪明，但是时间……
# 3.别人的答案，O(n)