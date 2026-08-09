class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        previousRow = [0] * n
        for _ in range(m - 1, -1, -1):
            currentRow = [0] * (n - 1) + [1]
            for columnIndex in range(n - 2, -1, -1):
                currentRow[columnIndex] = previousRow[columnIndex] + currentRow[columnIndex + 1]
            previousRow = currentRow
        return previousRow[0]
