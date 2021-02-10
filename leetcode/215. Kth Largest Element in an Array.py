import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        # 堆
        heap=nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            heapq.heappushpop(heap,i)
        return heap[0]