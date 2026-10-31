class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        numberOfRows = len(matrix)
        numberOfColumns = len(matrix[0])
        self.prefixSumsMatrix = [[]]

        firstRowPrefixSum = 0
        for columnIndex in range(len(matrix[0])):
            firstRowPrefixSum += matrix[0][columnIndex]
            self.prefixSumsMatrix[0].append(firstRowPrefixSum)

        for rowIndex in range(1, len(matrix)):
            self.prefixSumsMatrix.append([self.prefixSumsMatrix[rowIndex - 1][0] + matrix[rowIndex][0]])
            for columnIndex in range(1, len(matrix[0])):
                self.prefixSumsMatrix[rowIndex].append(
                    self.prefixSumsMatrix[rowIndex][columnIndex - 1] + 
                    self.prefixSumsMatrix[rowIndex - 1][columnIndex] -
                    self.prefixSumsMatrix[rowIndex - 1][columnIndex - 1] +
                    matrix[rowIndex][columnIndex]
                    )

        print(matrix)
        print(self.prefixSumsMatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        regionWidth = col2 - col1 + 1
        regionHeight = row2 - row1 + 1

        regionSum = self.prefixSumsMatrix[row2][col2]
        if col1 > 0:
            regionSum -= self.prefixSumsMatrix[row2][col2 - regionWidth]
        if row1 > 0:
            regionSum -= self.prefixSumsMatrix[row2 - regionHeight][col2]
        if row1 > 0 and col1 > 0:
            regionSum += self.prefixSumsMatrix[row2 - regionHeight][col2 - regionWidth]
        return regionSum