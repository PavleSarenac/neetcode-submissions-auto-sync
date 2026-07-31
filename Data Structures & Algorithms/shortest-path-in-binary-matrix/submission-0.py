class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(initialRow, initialColumn, pathLength) -> int:
            if grid[initialRow][initialColumn] != 0:
                return -1

            END_ROW, END_COLUMN = len(grid) - 1, len(grid[0]) - 1
            if initialRow == END_ROW and initialColumn == END_COLUMN:
                return pathLength

            ROW_WEST, ROW_NORTH, ROW_EAST, ROW_SOUTH = 0, -1, 0, 1
            ROW_NORTHWEST, ROW_NORTHEAST, ROW_SOUTHEAST, ROW_SOUTHWEST = -1, -1, 1, 1
            COLUMN_WEST, COLUMN_NORTH, COLUMN_EAST, COLUMN_SOUTH = -1, 0, 1, 0
            COLUMN_NORTHWEST, COLUMN_NORTHEAST, COLUMN_SOUTHEAST, COLUMN_SOUTHWEST = -1, 1, 1, -1
            directions = [
                (ROW_WEST, COLUMN_WEST),
                (ROW_NORTHWEST, COLUMN_NORTHWEST),
                (ROW_NORTH, COLUMN_NORTH),
                (ROW_NORTHEAST, COLUMN_NORTHEAST),
                (ROW_EAST, COLUMN_EAST),
                (ROW_SOUTHEAST, COLUMN_SOUTHEAST),
                (ROW_SOUTH, COLUMN_SOUTH),
                (ROW_SOUTHWEST, COLUMN_SOUTHWEST)
            ]

            LAND_VISITED = 2

            landCells = deque()
            grid[initialRow][initialColumn] = LAND_VISITED
            landCells.append((initialRow, initialColumn, pathLength))

            while landCells:
                currentRow, currentColumn, currentPathLength = landCells.popleft()
                for direction in directions:
                    nextRow = currentRow + direction[0]
                    nextColumn = currentColumn + direction[1]
                    if nextRow < 0 or nextRow > END_ROW or nextColumn < 0 or nextColumn > END_COLUMN or grid[nextRow][nextColumn] != 0:
                        continue
                    if nextRow == END_ROW and nextColumn == END_COLUMN:
                        return currentPathLength + 1
                    grid[nextRow][nextColumn] = LAND_VISITED
                    landCells.append((nextRow, nextColumn, currentPathLength + 1))
            return -1

        return bfs(0, 0, 1)