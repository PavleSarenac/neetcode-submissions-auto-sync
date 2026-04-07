class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            replacement = 0
            for j in range(i + 1, len(arr)):
                replacement = max(replacement, arr[j])
            arr[i] = replacement
        arr[-1] = -1
        return arr