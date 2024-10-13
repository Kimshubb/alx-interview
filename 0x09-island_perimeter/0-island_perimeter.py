#!/usr/bin/python3
"""Dsa Interview
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.    
    Parameters:
    - grid: List of lists representing the map where 0 is water and 1 is land.
    Returns:
    - Integer representing the perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Only consider land cells
            if grid[i][j] == 1:
                # Check all four sides
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
