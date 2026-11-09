class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        upperBound = pow(2, (len(nums) + 1) // 2 + 1)
        bitMask = 0
        for i in range(len(nums)):
            bitMask ^= nums[i]
        for number in range(len(nums) + 1, upperBound):
            bitMask ^= number
        return bitMask