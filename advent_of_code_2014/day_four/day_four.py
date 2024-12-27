"""Script containing the solutions to day 4."""

import hashlib

def hash_converter(key: str, part_two=False) -> str:
    """Returns numbers after the key that correspond to
    the MD5 hash that has 5 (False) or 6 (True) leading 0's"""

    found = False
    i = 0

    string = key
    while not found:

        hash_string = hashlib.md5(string.encode()).hexdigest()

        if not part_two:
            if hash_string[0:5] == "00000":
                found = True

        else:
            if hash_string[0:6] == "000000":
                found = True

        string = key + str(i)
        i += 1

    return i - 2

if __name__ == '__main__':

    print(hash_converter('ckczppom', True))
