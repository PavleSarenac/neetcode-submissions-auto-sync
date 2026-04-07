class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        scannedNumbers = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in scannedNumbers.keys():
                return [scannedNumbers[difference], i]
            scannedNumbers[nums[i]] = i