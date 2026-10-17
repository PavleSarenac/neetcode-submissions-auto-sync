class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        currentMaxSum, maxSum = 0, nums[0]
        currentMinSum, minSum = 0, nums[0]
        for number in nums:
            totalSum += number

            currentMaxSum = max(currentMaxSum + number, number)
            maxSum = max(currentMaxSum, maxSum)

            currentMinSum = min(currentMinSum + number, number)
            minSum = min(currentMinSum, minSum)

        return max(maxSum, totalSum - minSum) if maxSum > 0 else maxSum