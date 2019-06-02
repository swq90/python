def maxSubArray(nums) -> int:
    curSum = nums[0]
    maxSum = sum(nums)

    # curSum = maxSum = A[0]
    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum
    return maxSum
a=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray([-1,-2]))
