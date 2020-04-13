def maxSubArray(nums) -> int:
    curSum = nums[0]
    maxSum = sum(nums)

    # curSum = maxSum = A[0]
    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum


