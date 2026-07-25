class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]

        def dfs(row, column):
            if row < 0 or row >= len(image) or column < 0 or column >= len(image[0]) or image[row][column] != originalColor or image[row][column] == color:
                return

            image[row][column] = color    

            dfs(row, column - 1)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row + 1, column)

        dfs(sr, sc)

        return image