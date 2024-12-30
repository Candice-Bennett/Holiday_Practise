"""Script containing functions for day four."""

import re

def find_horizontal(grid: list[str], reverse=False) -> int:
    """Returns the number of horizontal XMAS instances"""

    total_xmas = 0

    if not reverse:
        regex = re.compile(r'XMAS')
    else:
        regex = re.compile(r'SAMX')

    for line in grid:
        total_xmas += len(regex.findall(line))

    return total_xmas


def find_vertical(grid: list[str], reverse=False) -> int:
    """Returns the number of vertical XMAS instances"""

    rotated_grid = [''] * len(grid)

    #god I wish I could do this in MATLAB LOL
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            rotated_grid[j] += grid[i][j]

    return find_horizontal(rotated_grid, reverse)


def find_diagonal(grid: list[str], reverse=False) -> int:
    """Returns the number of diagonal XMAS instances"""

    total_xmas = 0

    if reverse:
        grid = grid[::-1]

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if (i + 4) <= len(grid) and (j + 4) <= len(grid[i]):
                if grid[i][j] == 'X':
                    if grid[i+1][j+1] == 'M':
                        if grid[i+2][j+2] == 'A':
                            if grid[i+3][j+3] == 'S':
                                total_xmas += 1

            if (i + 4) <= len(grid) and (j-3) >= 0:
                if grid[i][j] == 'X':
                    if grid[i+1][j-1] == 'M':
                        if grid[i+2][j-2] == 'A':
                            if grid[i+3][j-3] == 'S':
                                total_xmas += 1

    return total_xmas


def xmas_finder(grid: str) -> int:
    """Returns total count of XMAS in a string grid."""

    grid = grid.split('\n')

    return (find_horizontal(grid) + find_horizontal(grid, True) +
            find_vertical(grid) + find_vertical(grid, True) +
            find_diagonal(grid) + find_diagonal(grid, True))

if __name__ == "__main__":

    with open('day_four_input.txt', 'r', encoding='UTF-8') as file:
        input_data = file.read()

    print(xmas_finder(input_data))
