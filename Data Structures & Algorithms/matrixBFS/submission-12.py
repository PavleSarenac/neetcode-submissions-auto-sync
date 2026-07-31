class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def bfs(initialRow, initialColumn, pathLength) -> int:
            if grid[initialRow][initialColumn] != 0:
                return -1

            END_ROW, END_COLUMN = len(grid) - 1, len(grid[0]) - 1
            if initialRow == END_ROW and initialColumn == END_COLUMN:
                return pathLength

            LAND_VISITED = 2

            landCells = deque()
            grid[initialRow][initialColumn] = LAND_VISITED
            landCells.append((initialRow, initialColumn, pathLength))

            ROW_LEFT, ROW_UP, ROW_RIGHT, ROW_DOWN = 0, -1, 0, 1
            COLUMN_LEFT, COLUMN_UP, COLUMN_RIGHT, COLUMN_DOWN = -1, 0, 1, 0
            directions = [
                (ROW_LEFT, COLUMN_LEFT),
                (ROW_UP, COLUMN_UP),
                (ROW_RIGHT, COLUMN_RIGHT),
                (ROW_DOWN, COLUMN_DOWN)
            ]

            while landCells:
                currentLandCell = landCells.popleft()
                currentRow = currentLandCell[0]
                currentColumn = currentLandCell[1]
                currentPathLength = currentLandCell[2]

                for direction in directions:
                    nextRow = currentRow + direction[0]
                    nextColumn = currentColumn + direction[1]
                    isNextRowInvalid = nextRow < 0 or nextRow >= len(grid)
                    isNextColumnInvalid = nextColumn < 0 or nextColumn >= len(grid[0])
                    if isNextRowInvalid or isNextColumnInvalid or grid[nextRow][nextColumn] != 0:
                        continue
                    if nextRow == END_ROW and nextColumn == END_COLUMN:
                        return currentPathLength + 1
                    grid[nextRow][nextColumn] = LAND_VISITED
                    landCells.append((nextRow, nextColumn, currentPathLength + 1))

            return -1

        return bfs(0, 0, 0)