class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxesToDigitsMap = [set() for _ in range(9)]
        rowsToDigitsMap = [set() for _ in range(9)]
        columnsToDigitsMap = [set() for _ in range(9)]

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == ".":
                    continue

                subBoxIndex = (row // 3) * 3 + (column // 3)
                if board[row][column] in subBoxesToDigitsMap[subBoxIndex]:
                    return False
                subBoxesToDigitsMap[subBoxIndex].add(board[row][column])

                if board[row][column] in rowsToDigitsMap[row]:
                    return False
                rowsToDigitsMap[row].add(board[row][column])

                if board[row][column] in columnsToDigitsMap[column]:
                    return False
                columnsToDigitsMap[column].add(board[row][column])
        return True
                