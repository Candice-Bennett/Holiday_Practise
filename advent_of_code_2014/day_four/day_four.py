"""Script containing the solutions to day 4."""

import hashlib

def hash_converter(key: str) -> str:
    """Returns the thing that this problem is asking for"""

    found = False
    i = 0

    string = key
    while not found:

        hash_string = hashlib.md5(string.encode()).hexdigest()

        if hash_string[0:5] == "00000":
            found = True
            break

        string = key + str(i)
        i += 1

    return i - 1

if __name__ == '__main__':

    print(hash_converter('ckczppom'))
