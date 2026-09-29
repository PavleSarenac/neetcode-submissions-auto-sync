class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        numberOfRows = len(text1)
        numberOfColumns = len(text2)
        dp = [0] * (numberOfColumns + 1)
        for row in range(numberOfRows - 1, -1, -1):
            diagonal = dp[-1]
            for column in range(numberOfColumns - 1, -1, -1):
                down = dp[column]
                right = dp[column + 1]
                if text1[row] == text2[column]:
                    dp[column] = 1 + diagonal
                else:
                    dp[column] = max(down, right)
                diagonal = down
        return dp[0]
