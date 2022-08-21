#!/usr/bin/python3
"""
Grid cells are connected horizontally/vertically
"""


def island_perimeter(grid):
    """there is only one island(or nothing)"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                # Each cell is square, with a side lengeth of 1
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # cells are connected horizontally/vertically(not diagonally)
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
