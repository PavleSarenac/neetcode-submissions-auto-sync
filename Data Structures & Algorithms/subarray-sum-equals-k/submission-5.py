class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumsHistory = dict()
        prefixSumsHistory[0] = 1

        prefixSum = 0
        kSumCount = 0

        for subarrayEndIndex in range(len(nums)):
            prefixSum += nums[subarrayEndIndex]
            complementPrefixSum = prefixSum - k
            
            totalPossibleSubarrayStartIndices = prefixSumsHistory.get(complementPrefixSum, 0)
            kSumCount += totalPossibleSubarrayStartIndices

            prefixSumsHistory[prefixSum] = prefixSumsHistory.get(prefixSum, 0) + 1

        return kSumCount