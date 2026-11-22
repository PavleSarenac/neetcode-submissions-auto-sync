class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        largeInteger = 0
        digitSignificance = 1
        for i in range(len(digits) - 1, -1, -1):
            largeInteger += digitSignificance * digits[i]
            digitSignificance *= 10
        largeInteger += 1

        largeInteger = str(largeInteger)
        result = []
        for digit in largeInteger:
            result.append(int(digit))
            
        return result