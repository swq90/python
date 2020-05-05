def maxSubArray(nums) -> int:
    # curSum = nums[0]
    # maxSum = sum(nums)

    curSum=maxSum=nums[0]
    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum

nums=[-1,-2,]
z=maxSubArray(nums)
print(z)
