class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        writeIndex = 0
        for readIndex in range(len(nums)):
            if writeIndex > 0 and nums[writeIndex - 1] == nums[readIndex]:
                continue
            nums[writeIndex] = nums[readIndex]
            writeIndex += 1
        return writeIndex