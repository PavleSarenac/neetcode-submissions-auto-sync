class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, column):
            if int(row) < 0 or int(row) >= len(grid) or int(column) < 0 or int(column) >= len(grid[0]) or grid[row][column] == '0':
                return

            grid[row][column] = '0'
            
            dfs(row, column - 1)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row + 1, column)

        numberOfIslands = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == '1':
                    numberOfIslands += 1
                    dfs(row, column)

        return numberOfIslands