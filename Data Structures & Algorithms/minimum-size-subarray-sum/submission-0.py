class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimumSubarrayLength = len(nums) + 1
        currentSum = 0
        leftWindowEdge = rightWindowEdge = 0

        for currentNumber in nums:
            currentSum += currentNumber
            rightWindowEdge += 1
            while currentSum >= target:
                minimumSubarrayLength = min(minimumSubarrayLength, rightWindowEdge - leftWindowEdge)
                currentSum -= nums[leftWindowEdge]
                leftWindowEdge += 1

        if minimumSubarrayLength > len(nums):
            minimumSubarrayLength = 0
        return minimumSubarrayLength