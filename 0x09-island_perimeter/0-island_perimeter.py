#!/usr/bin/python3
"""Module contains a function island_perimeter
that returns the perimeter of the island described
by the grid"""


def island_perimeter(grid):
    """returns the perimeter of the
    island described by the grid

    Args:
        grid: list[list]
    Returns:
        perimeter: int
    """
    gridLen = len(grid)
    rowLen = len(grid[0])
    perimeter = 0
    for i in range(gridLen):
        row = grid[i]
        for j in range(rowLen):
            if row[j] == 0:
                continue

            square = 4
            left = j - 1
            right = j + 1
            up = i - 1
            down = i + 1

            if left >= 0:
                if row[left] == 1:
                    square -= 1
            if right < rowLen:
                if row[right] == 1:
                    square -= 1
            if up >= 0:
                if grid[up][j] == 1:
                    square -= 1
            if down < gridLen:
                if grid[down][j] == 1:
                    square -= 1

            perimeter += square
    return perimeter
