class Solution:
    def reverseBits(self, n: int) -> int:
        maxBitIndex = 31
        reversedNumber = 0x00000000
        for i in range(0, 16):
            lowerBitIndex = i
            upperBitIndex = (maxBitIndex - i)

            lowerBitChoiceMask = 0x00000001 << lowerBitIndex
            upperBitChoiceMask = 0x00000001 << upperBitIndex

            lowerBit = (n & lowerBitChoiceMask) >> lowerBitIndex
            upperBit = (n & upperBitChoiceMask) >> upperBitIndex

            swappedBitsMask = (upperBit << lowerBitIndex) | (lowerBit << upperBitIndex)

            reversedNumber |= swappedBitsMask
        return reversedNumber