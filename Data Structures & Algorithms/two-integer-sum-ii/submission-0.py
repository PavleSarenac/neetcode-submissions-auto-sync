class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer, rightPointer = 0, len(numbers) - 1
        while leftPointer < rightPointer:
            twoSum = numbers[leftPointer] + numbers[rightPointer]
            if twoSum == target:
                return [leftPointer + 1, rightPointer + 1]
            if twoSum < target:
                leftPointer += 1
            else:
                rightPointer -= 1