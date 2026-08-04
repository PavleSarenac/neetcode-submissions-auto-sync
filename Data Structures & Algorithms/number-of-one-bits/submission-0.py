class Solution:
    def hammingWeight(self, n: int) -> int:
        numberOfOneBits = 0
        while n > 0:
            numberOfOneBits += n & 1
            n >>= 1
        return numberOfOneBits