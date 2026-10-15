class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        leftEnd, rightEnd = 0, len(nums) - 1
        for leftEnd in range(len(nums)):
            currentSum = 0
            rightEnd = leftEnd
            for _ in range(len(nums)):
                currentSum = max(currentSum + nums[rightEnd], nums[rightEnd])
                maxSum = max(currentSum, maxSum)
                rightEnd = (rightEnd + 1) % len(nums)
        return maxSum