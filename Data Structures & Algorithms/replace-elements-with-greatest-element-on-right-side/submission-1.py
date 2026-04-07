class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = -1
        for i in range(len(arr) - 1, 0, -1):
            tmp = arr[i - 1]
            arr[i - 1] = max(prev, arr[i])
            prev = tmp
        arr[len(arr) - 1] = -1
        return arr