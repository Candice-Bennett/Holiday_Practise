"""Script containing functions for day four."""

#Notes: could use [::-1] to reverse the input string to find reverse strings
#       that way would only need find horizontal, vertical, diagonal and just
#       input correct and reversed?

import re

def find_horizontal(grid: list[str], reverse=False) -> int:
    """Returns the number of horizontal XMAS instances"""
    
    total_xmas = 0
    regex = re.compile(r'XMAS')
    for line in grid:
        total_xmas += len(regex.findall(line))
    
    return total_xmas


def find_vertical(grid: list[str], reverse=False) -> int:
    """Returns the number of vertical XMAS instances"""
    ...


def find_diagonal(grid: list[str], reverse=False) -> int:
    """Returns the number of diagonal XMAS instances"""
    ...

if __name__ == "__main__":

    with open('day_four_input.txt', 'r', encoding='UTF-8') as file:
        input_data = file.read()
    
    split_data = input_data.split('\n')
    for line in split_data:
        print(line)

