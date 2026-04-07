class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colorCounters = [0, 0, 0]
        for num in nums:
            colorCounters[num] += 1

        arrayIndex = 0
        for color in range(len(colorCounters)):
            for _ in range(colorCounters[color]):
                nums[arrayIndex] = color
                arrayIndex += 1