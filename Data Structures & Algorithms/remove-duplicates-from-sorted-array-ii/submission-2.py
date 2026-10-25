class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writeIndex = 0
        for readIndex in range(len(nums)):
            if readIndex > 1 and nums[writeIndex - 2] == nums[readIndex]:
                continue
            nums[writeIndex] = nums[readIndex]
            writeIndex += 1
        return writeIndex