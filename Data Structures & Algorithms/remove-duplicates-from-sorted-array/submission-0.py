class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        k = 1
        currentElement = nums[0]
        currentWriteIndex = 1
        for currentReadIndex in range(1, len(nums)):
            if nums[currentReadIndex] == currentElement:
                continue
            currentElement = nums[currentReadIndex]
            nums[currentWriteIndex] = currentElement
            currentWriteIndex += 1
            k += 1
        return k
