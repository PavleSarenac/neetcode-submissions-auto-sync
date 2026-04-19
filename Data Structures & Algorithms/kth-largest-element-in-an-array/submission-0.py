class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for numIndex in range(len(nums)):
            heapq.heappush(minHeap, nums[numIndex])
            if numIndex >= k:
                heapq.heappop(minHeap)
        return minHeap[0]
