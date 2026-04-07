# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, start, pivot):
        if pivot <= start:
            return
        
        lessThanPivotIndex = start
        for i in range(start, pivot + 1):
            if pairs[i].key >= pairs[pivot].key:
                continue
            if i != lessThanPivotIndex:
                self.swap(pairs, lessThanPivotIndex, i)
            lessThanPivotIndex += 1
        if lessThanPivotIndex != pivot:
            self.swap(pairs, lessThanPivotIndex, pivot)

        self.quickSortHelper(pairs, start, lessThanPivotIndex - 1)
        self.quickSortHelper(pairs, lessThanPivotIndex + 1, pivot)

    def swap(self, pairs, i, j):
        tmp = pairs[i]
        pairs[i] = pairs[j]
        pairs[j] = tmp