class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return len(arr)

        maxSubarrayLength = 1
        leftWindowEdge = 0
        
        isPreviousSmaller = (arr[1] - arr[0] > 0)
        for rightWindowEdge in range(1, len(arr)):
            difference = arr[rightWindowEdge] - arr[rightWindowEdge - 1]
            if difference == 0:
                leftWindowEdge = rightWindowEdge
                isPreviousSmaller = False
            elif (isPreviousSmaller and difference < 0) or (not isPreviousSmaller and difference > 0):
                leftWindowEdge = rightWindowEdge - 1
                maxSubarrayLength = max(maxSubarrayLength, rightWindowEdge - leftWindowEdge + 1)
            else:
                isPreviousSmaller = not isPreviousSmaller
                maxSubarrayLength = max(maxSubarrayLength, rightWindowEdge - leftWindowEdge + 1)

        return maxSubarrayLength