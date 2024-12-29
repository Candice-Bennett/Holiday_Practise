"""Script containing functions for advent of code day 3"""
import re

def filter_corrupted_memory(string: str) -> list[str]:
    """Filters the code for mul(x,y) where x and y are 1-3 digit numbers"""

    regex = re.compile(r'mul\(\d\d?\d?,\d\d?\d?\)')
    return regex.findall(string)


def interpret_data(data: list[str]) -> list[list[int]]:
    """Takes the filtered data and turns it into two numbers to multiply"""

    numbers = []
    for recovered_data in data:
        first_step_clean = recovered_data[4:-1]
        split_data = first_step_clean.split(',')
        numbers.append(split_data)

    return numbers


def mul(x: str, y: str) -> int:
    """Returns the product of two numbers x and y."""

    return int(x) * int(y)


def day_three_first_pt(input_data: str) -> int:
    """Produces the sum of all the uncorrupted data."""

    cleaned_data = filter_corrupted_memory(input_data)
    numbers = interpret_data(cleaned_data)

    sum_of_mul = 0

    for number in numbers:
        sum_of_mul += mul(number[0],number[1])

    return sum_of_mul

if __name__ == "__main__":

    with open('day_three_input.txt','r',encoding='UTF-8') as file:
        day_three_input = file.read()

    print(day_three_first_pt(day_three_input))
