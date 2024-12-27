"""File containing solutions to advent of code 2014 day two."""

import re

def surface_area(dimensions_string: str) -> int:
    """Takes the three dimensions of an object and 
    returns the area of wrapping paper needed."""

    


def validate_surface_area(dimensions: list[int]) -> bool:
    """Returns whether input is of valid format."""
    
    if not isinstance(dimensions, list):
        return False

    if not len(dimensions) == 3:
        return False

    if not dimensions[0].isdigit():
        return False

    if not dimensions[1].isdigit():
        return False

    if not dimensions[2].isdigit():
        return False

    return True


def convert_data(string: str) -> list[int]:
    """Returns an array with values from input string of form AxBxC
    Where A, B and C are numbers"""
    
    if not isinstance(string, str):
        raise ValueError('Input must be a string.')

    if not re.match('^\d+(\.\d+)?x\d+(\.\d+)?x\d+(\.\d+)?$', string):
        raise ValueError('Input must be a string of format AxBxC where A, B and C are numbers.')

    return float(string.split('x'))

#I have greatly over complicated this!
if __name__ == "__main__":
    ...
