class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxSumPreviousPrevious = nums[0]
        maxSumPrevious = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            oldMaxSumPrevious = maxSumPrevious
            maxSumPrevious = max(maxSumPrevious, nums[i] + maxSumPreviousPrevious)
            maxSumPreviousPrevious = oldMaxSumPrevious

        return maxSumPrevious
        