class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        currentWriteIndex = 0
        for currentReadIndex in range(len(nums)):
            if nums[currentReadIndex] != val:
                nums[currentWriteIndex] = nums[currentReadIndex]
                currentWriteIndex += 1
        return currentWriteIndex