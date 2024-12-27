"""File containing solutions to advent of code 2014 day two."""

import re

def surface_area(dimensions_string: str) -> int:
    """Takes the three dimensions of an object and 
    returns the area of wrapping paper needed."""

    dimensions = convert_data(dimensions_string)

    if not validate_surface_area(dimensions):
        raise TypeError('Input must be of form AxBxC where A, B and C are all numbers.')

    length_width = dimensions[0] * dimensions[1]
    width_height = dimensions[1] * dimensions[2]
    height_length = dimensions[2] * dimensions[0]

    if length_width <= width_height and length_width <= height_length:
        smallest = length_width

    if width_height <= length_width and width_height <= height_length:
        smallest = width_height

    if height_length <= width_height and height_length <= length_width:
        smallest = height_length

    return 2 * (length_width + width_height + height_length) + smallest


def validate_surface_area(dimensions: list[int]) -> bool:
    """Returns whether input is of valid format."""

    if not isinstance(dimensions, list):
        return False

    if not len(dimensions) == 3:
        return False

    if not isinstance(dimensions[0], (float, int)):
        return False

    if not isinstance(dimensions[1], (float, int)):
        return False


    if not isinstance(dimensions[2], (float, int)):
        return False

    return True


def convert_data(string: str) -> list[int]:
    """Returns an array with values from input string of form AxBxC
    Where A, B and C are numbers"""

    if not isinstance(string, str):
        raise ValueError('Input must be a string.')

    if not re.match(r'^\d+(\.\d+)?x\d+(\.\d+)?x\d+(\.\d+)?$', string):
        raise ValueError('Input must be a string of format AxBxC where A, B and C are numbers.')

    result = string.split('x')

    for i in range(len(result)):
        result[i] = float(result[i])

    return result


def ribbon_calculator(dimensions_string: str) -> int:
    """Returns the amount of ribbon needed for set dimensions"""

#I have greatly over complicated this!
if __name__ == "__main__":

    with open('day_two_input.txt', 'r', encoding='UTF-8') as file:
        input_data = file.read()

    input_data = input_data.split('\n')

    total_sum = 0
    for present in input_data:

        total_sum += surface_area(present)

    print(total_sum)
