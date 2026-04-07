# Time complexity of this solution is O(n * log(n)) - it is optimal for merge sort
# Space complexity of this solution is O(n + log(n)) ~ O(n) - it is optimal for merge sort

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

from typing import List

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    
    def mergeSortHelper(self, originalArray, startIndex, endIndex) -> List[Pair]:
        if startIndex >= endIndex:
            return originalArray
        
        middleIndex = (startIndex + endIndex) // 2

        self.mergeSortHelper(originalArray, startIndex, middleIndex)
        self.mergeSortHelper(originalArray, middleIndex + 1, endIndex)

        self.merge(originalArray, startIndex, middleIndex, endIndex)

        return originalArray

    def merge(self, originalArray, startIndex, middleIndex, endIndex):
        leftSubArray = originalArray[startIndex : middleIndex + 1]
        rightSubArray = originalArray[middleIndex + 1: endIndex + 1]

        originalArrayIndex = startIndex
        leftSubArrayIndex = rightSubArrayIndex = 0

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