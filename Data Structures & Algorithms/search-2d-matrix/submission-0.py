class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row = self.findRow(matrix, target)
        if row == -1:
            return False
        
        column = self.findColumn(matrix[row], target)
        if column == -1:
            return False
        
        return True

        
    def findRow(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m - 1

        while start <= end:
            middle = (start + end) // 2
            if matrix[middle][0] > target:
                end = middle - 1
            elif matrix[middle][n - 1] < target:
                start = middle + 1
            else:
                return middle
            
        return -1
    
    def findColumn(self, row: List[int], target: int) -> int:
        start = 0
        end = len(row) - 1

        while start <= end:
            middle = (start + end) // 2
            if row[middle] > target:
                end = middle - 1
            elif row[middle] < target:
                start = middle + 1
            else:
                return middle
            
        return -1