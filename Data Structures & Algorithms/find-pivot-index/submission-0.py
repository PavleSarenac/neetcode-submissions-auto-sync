class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = [nums[0]]
        for i in range(1, len(nums)):
            prefixSums.append(prefixSums[i - 1] + nums[i])

        suffixSums = [nums[len(nums) - 1]]
        for i in range(len(nums) - 2, -1, -1):
            suffixSums.insert(0, suffixSums[0] + nums[i])

        for i in range(len(nums)):
            leftSum = rightSum = 0
            if i > 0:
                leftSum = prefixSums[i - 1]
            if i < len(nums) - 1:
                rightSum = suffixSums[i + 1]
            if leftSum == rightSum:
                return i
        return -1