class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i in range(len(nums)):
            pairIndex = hashMap.get(nums[i])
            if pairIndex is not None:
                return [pairIndex, i]
            else:
                hashMap[target - nums[i]] = i