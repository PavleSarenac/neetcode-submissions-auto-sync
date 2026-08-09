class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        for columnIndex in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][columnIndex] == 1:
                break
            dp[columnIndex] = 1
        for rowIndex in range(m - 2, -1, -1):
            if obstacleGrid[rowIndex][n - 1] == 1:
                dp[n - 1] = 0
            for columnIndex in range(n - 2, -1, -1):
                if obstacleGrid[rowIndex][columnIndex] == 1:
                    dp[columnIndex] = 0
                else:
                    dp[columnIndex] += dp[columnIndex + 1]
        return dp[0]