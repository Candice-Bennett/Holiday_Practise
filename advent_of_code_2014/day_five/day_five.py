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
            print(i)
            print(string[i])
            return True
    
    return False


def validate_bad_string(string: str) -> bool:
    """Ensures disallowed substrings are not in string"""
    ...

if __name__ == "__main__":

    print(validate_double_letters('shouldnt work'))