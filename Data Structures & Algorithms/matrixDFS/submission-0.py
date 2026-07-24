class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.totalUniquePaths = 0

        def dfs(grid, row, column):
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] != 0:
                return
            if row == len(grid) - 1 and column == len(grid[0]) - 1 and grid[row][column] == 0:
                self.totalUniquePaths += 1
                return
            
            originalValue = grid[row][column]
            grid[row][column] = 2

            dfs(grid, row, column - 1)
            dfs(grid, row - 1, column)
            dfs(grid, row, column + 1)
            dfs(grid, row + 1, column)

            grid[row][column] = originalValue

        dfs(grid, 0, 0)

        return self.totalUniquePaths