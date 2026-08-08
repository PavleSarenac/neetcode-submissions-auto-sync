class Solution:
    def reverseBits(self, n: int) -> int:
        minBitIndex = 0
        maxBitIndex = 31
        reversedNumber = 0x00000000
        for i in range(minBitIndex, (maxBitIndex + 1) >> 1):
            lowerBitIndex = i
            upperBitIndex = (maxBitIndex - i)

            lowerBitChoiceMask = 0x00000001 << lowerBitIndex
            upperBitChoiceMask = 0x00000001 << upperBitIndex

            lowerBit = (n & lowerBitChoiceMask) >> lowerBitIndex
            upperBit = (n & upperBitChoiceMask) >> upperBitIndex

            swappedBitsMask = (upperBit << lowerBitIndex) | (lowerBit << upperBitIndex)

            reversedNumber |= swappedBitsMask
        return reversedNumber