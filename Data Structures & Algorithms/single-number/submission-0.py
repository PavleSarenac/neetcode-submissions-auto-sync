class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitMask = 0
        for num in nums:
            bitMask ^= num
        return bitMask
