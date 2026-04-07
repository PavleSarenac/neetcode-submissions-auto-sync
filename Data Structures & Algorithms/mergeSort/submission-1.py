# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        startIndex = 0
        middleIndex = len(pairs) // 2
        endIndex = len(pairs) - 1

        if startIndex >= endIndex:
            return pairs

        leftSubArray = pairs[startIndex:middleIndex]
        rightSubArray = pairs[middleIndex:endIndex + 1]

        self.mergeSort(leftSubArray)
        self.mergeSort(rightSubArray)

        return self.merge(
            pairs,
            leftSubArray, 
            rightSubArray
            )

    def merge(
        self,
        originalArray,
        leftSubArray,
        rightSubArray
        ) -> List[Pair]:
        originalArrayIndex = leftSubArrayIndex = rightSubArrayIndex = 0

        while leftSubArrayIndex < len(leftSubArray) and rightSubArrayIndex < len(rightSubArray):
            if leftSubArray[leftSubArrayIndex].key <= rightSubArray[rightSubArrayIndex].key:
                originalArray[originalArrayIndex] = leftSubArray[leftSubArrayIndex]
                leftSubArrayIndex += 1
            else:
                originalArray[originalArrayIndex] = rightSubArray[rightSubArrayIndex]
                rightSubArrayIndex += 1
            originalArrayIndex += 1

        while leftSubArrayIndex < len(leftSubArray):
            originalArray[originalArrayIndex] = leftSubArray[leftSubArrayIndex]
            originalArrayIndex += 1
            leftSubArrayIndex += 1

        while rightSubArrayIndex < len(rightSubArray):
            originalArray[originalArrayIndex] = rightSubArray[rightSubArrayIndex]
            originalArrayIndex += 1
            rightSubArrayIndex += 1

        return originalArray