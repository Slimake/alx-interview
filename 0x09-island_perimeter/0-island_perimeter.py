#!/usr/bin/python3
"""0-island_perimeter module
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid
    """
    # Get the length of row and column
    row, column = len(grid), len(grid[0])
    perimeter = 0

    # Loop through rows and columns
    for i in range(row):
        for j in range(column):
            # if the cell is 1(i.e land)
            if grid[i][j] == 1:
                # if it's the first row or top cell equal 0
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # if it's the last row or bottom cell equal 0
                if i == row - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # if it's the first column or left cell equal 0
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == column - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
