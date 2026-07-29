class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND_VISITED = 2

        def dfs(row, column):
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] != 1:
                return

            grid[row][column] = LAND_VISITED
            self.area += 1
            
            dfs(row, column - 1)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row + 1, column)

        maxArea = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                self.area = 0
                dfs(row, column)
                if self.area > maxArea:
                    maxArea = self.area

        return maxArea