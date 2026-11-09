class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingNumber = len(nums)
        for i in range(len(nums)):
            missingNumber ^= i ^ nums[i]
        return missingNumber