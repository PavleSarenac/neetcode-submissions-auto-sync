class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        tallestLeftBar, tallestRightBar = height[0], height[len(height) - 1]
        currentLeftBar, currentRightBar = 0, len(height) - 1
        while currentLeftBar < currentRightBar:
            if tallestLeftBar < tallestRightBar:
                currentLeftBar += 1
                totalWater += max(0, (tallestLeftBar - height[currentLeftBar]))
                tallestLeftBar = max(tallestLeftBar, height[currentLeftBar])
            else:
                currentRightBar -= 1
                totalWater += max(0, (tallestRightBar - height[currentRightBar]))
                tallestRightBar = max(tallestRightBar, height[currentRightBar])
        return totalWater