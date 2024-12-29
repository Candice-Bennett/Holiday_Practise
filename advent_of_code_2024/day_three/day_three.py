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


def filter_corrupted_memory_pt_two(string: str) -> list[str]:
    """Filters the string for mult(), do() and don't() functions."""

    regex =  re.compile(r'mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)')
    return regex.findall(string)


def run_do_dont_commands(data: list[str]) -> list[str]:
    """Removes all mul() commands preceded by a don't()."""

    do = True
    return_data = []

    for value in data:
        if value == "do()":
            do = True
        elif value == "don't()":
            do = False
        elif value != "do()" and do:
            return_data.append(value)

    return return_data


def day_three_second_pt(input_data: str) -> int:
    """Returns the solution to day three part 2."""

    cleaned_data = filter_corrupted_memory_pt_two(input_data)
    modified_data = run_do_dont_commands(cleaned_data)
    numbers = interpret_data(modified_data)

    sum_of_mul = 0

    for number in numbers:
        sum_of_mul += mul(number[0],number[1])

    return sum_of_mul

if __name__ == "__main__":

    with open('day_three_input.txt','r',encoding='UTF-8') as file:
        day_three_input = file.read()

    print(day_three_first_pt(day_three_input))
    print(day_three_second_pt(day_three_input))
