class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY_CELL, FRESH_FRUIT, ROTTEN_FRUIT = 0, 1, 2
    
        rottenFruits = deque()
        freshFruits = set()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == ROTTEN_FRUIT:
                    rottenFruits.append((row, column))
                if grid[row][column] == FRESH_FRUIT:
                    freshFruits.add((row, column))

        if not freshFruits:
            return 0
        if not rottenFruits:
            return -1

        ROW_LEFT, ROW_UP, ROW_RIGHT, ROW_DOWN = 0, -1, 0, 1
        COLUMN_LEFT, COLUMN_UP, COLUMN_RIGHT, COLUMN_DOWN = -1, 0, 1, 0
        directions = [
            (ROW_LEFT, COLUMN_LEFT),
            (ROW_UP, COLUMN_UP),
            (ROW_RIGHT, COLUMN_RIGHT),
            (ROW_DOWN, COLUMN_DOWN)
        ]

        minutes = -1
        while rottenFruits:
            for _ in range(len(rottenFruits)):
                currentRow, currentColumn = rottenFruits.popleft()
                for direction in directions:
                    nextRow = currentRow + direction[0]
                    nextColumn = currentColumn + direction[1]
                    if nextRow < 0 or nextRow >= len(grid) or nextColumn < 0 or nextColumn >= len(grid[0]) or grid[nextRow][nextColumn] != FRESH_FRUIT:
                        continue
                    freshFruits.remove((nextRow, nextColumn))
                    grid[nextRow][nextColumn] = ROTTEN_FRUIT
                    rottenFruits.append((nextRow, nextColumn))
            minutes += 1

        if freshFruits:
            return -1

        return minutes