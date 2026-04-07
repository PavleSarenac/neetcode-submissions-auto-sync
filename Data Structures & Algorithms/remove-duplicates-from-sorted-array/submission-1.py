class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        currentWriteIndex = 1
        for currentReadIndex in range(1, len(nums)):
            if nums[currentReadIndex] != nums[currentReadIndex - 1]:
                nums[currentWriteIndex] = nums[currentReadIndex]
                currentWriteIndex += 1
        return currentWriteIndex
