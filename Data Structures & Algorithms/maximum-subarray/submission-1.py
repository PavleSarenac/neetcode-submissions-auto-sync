class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        for number in nums:
            currentSum = max(currentSum + number, number) 
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum