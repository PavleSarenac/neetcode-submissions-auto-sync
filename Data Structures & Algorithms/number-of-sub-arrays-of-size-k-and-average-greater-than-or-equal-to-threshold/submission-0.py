class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        numberOfSubarrays = 0
        currentSum = 0
        for i in range(len(arr)):
            currentSum += arr[i]
            if i < k - 1:
                continue
            if currentSum / k >= threshold:
                numberOfSubarrays += 1
            currentSum -= arr[i - (k - 1)]
        return numberOfSubarrays