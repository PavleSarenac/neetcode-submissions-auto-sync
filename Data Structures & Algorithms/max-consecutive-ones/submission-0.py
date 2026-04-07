class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentConsecutiveOnes = maxConsecutiveOnes = 0
        for num in nums:
            if num == 1:
                currentConsecutiveOnes += 1
            else:
                if currentConsecutiveOnes > maxConsecutiveOnes:
                    maxConsecutiveOnes = currentConsecutiveOnes
                currentConsecutiveOnes = 0
        if currentConsecutiveOnes > maxConsecutiveOnes:
            maxConsecutiveOnes = currentConsecutiveOnes
        return maxConsecutiveOnes