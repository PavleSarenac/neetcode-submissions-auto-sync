class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftWindowEdge, rightWindowEdge = 0, len(heights) - 1
        maxArea = 0
        while leftWindowEdge < rightWindowEdge:
            width = rightWindowEdge - leftWindowEdge
            height = min(heights[leftWindowEdge], heights[rightWindowEdge])
            area = width * height
            maxArea = max(maxArea, area)
            if heights[leftWindowEdge] < heights[rightWindowEdge]:
                leftWindowEdge += 1
            else:
                rightWindowEdge -= 1
        return maxArea