class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum, maxSum = 0, nums[0]
        for number in nums:
            currentSum = max(currentSum + number, number)
            maxSum = max(currentSum, maxSum)
        return maxSum