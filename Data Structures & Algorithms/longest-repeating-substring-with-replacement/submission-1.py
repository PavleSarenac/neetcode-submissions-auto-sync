class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxSubarrayLength = 0
        leftWindowEdge = 0
        currentWindowLetterFrequency = dict()
        maxLetterFrequency = 0

        for rightWindowEdge in range(len(s)):
            currentWindowSize = rightWindowEdge - leftWindowEdge + 1
            if s[rightWindowEdge] not in currentWindowLetterFrequency.keys():
                currentWindowLetterFrequency[s[rightWindowEdge]] = 0
            currentWindowLetterFrequency[s[rightWindowEdge]] += 1
            maxLetterFrequency = max(maxLetterFrequency, currentWindowLetterFrequency[s[rightWindowEdge]])
            if currentWindowSize - maxLetterFrequency <= k:
                maxSubarrayLength = max(maxSubarrayLength, currentWindowSize)
            else:
                currentWindowLetterFrequency[s[leftWindowEdge]] -= 1
                leftWindowEdge += 1
            
        return maxSubarrayLength
