"""Contains the function for day five of 2014 advent of code"""

def validate_vowels(string: str) -> bool:
    """Checks that at least three vowels are present in a string"""

    vowels = ['a','e','i','o','u']
    vowel_count = 0

    for character in string:

        if character in vowels:
            vowel_count += 1

            if vowel_count >= 3:
                return True

    return False


def validate_double_letters(string: str) -> bool:
    """Checks a double letter appears in the string"""

    for i in range(len(string)-1):

        if string[i] == string[i+1]:
            return True

    return False


def validate_bad_string(string: str) -> bool:
    """Ensures disallowed substrings are not in string"""

    bad_strings = ['ab','cd','pq','xy']
    return not any(bad_string in string for bad_string in bad_strings)


def find_part_one(string: list[str]) -> None:
    """Prints number of valid strings"""

    valid_strings = 0

    for line in string:

        if validate_vowels(line) and validate_double_letters(line) and validate_bad_string(line):
            valid_strings += 1

    print(valid_strings)


def repeat_with_middle():
    '''Checks if string has something of for xyx'''
    ...


def two_letters_no_overlap():
    '''Checks if string has a pair of characters that repeats'''
    ...


def find_part_two(string):
    """Prints number of valid strings"""

    valid_strings = 0

    for line in string:

        if repeat_with_middle(line) and two_letters_no_overlap(line):
            valid_strings += 1

    print(valid_strings)

if __name__ == "__main__":

    with open('day_five_input.txt', 'r', encoding='UTF-8') as file:
        input_data = file.read()

    input_data = input_data.split('\n')
    find_part_one(input_data)


