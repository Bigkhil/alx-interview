#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom edge
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right edge
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter