"""Script containing functions for day four."""

#Notes: could use [::-1] to reverse the input string to find reverse strings
#       that way would only need find horizontal, vertical, diagonal and just
#       input correct and reversed?

import re

def find_horizontal(grid: list[str], reverse=False) -> int:
    """Returns the number of horizontal XMAS instances"""
    
    total_xmas = 0

    if not reverse:
        regex = re.compile(r'XMAS')
    else:
        regex = re.compile(r'SAMX')

    for line in grid:
        print(reverse)
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
    ...

if __name__ == "__main__":

    with open('day_four_input.txt', 'r', encoding='UTF-8') as file:
        input_data = file.read()

    split_data = input_data.split('\n')
    for line in split_data:
        print(line)

    print(len(split_data))
    print(len(line))

    new_grid = ['XXXXX',
                'MMMMM',
                'AAAAA',
                'SSSSS',
                'XXXXX']

    print(new_grid)
    find_vertical(new_grid)