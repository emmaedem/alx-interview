
#!/usr/bin/python3
"""
module that calculate perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Parameters:
    grid (list of list of int): The grid representation where 0 is water and 1 is land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):

        for j in range(len(grid[i])):
            if grid[i][j] == 1:
              
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1

                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1

                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

                if j == len(grid[i]) - 1 or grid[i][j+1] == 0: 
                    perimeter += 1
    return perimeter

