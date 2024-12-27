"""Script containing the solutions to day 4."""

import hashlib

def hash_converter(key: str) -> str:
    """Returns the thing that this problem is asking for"""

    found = False
    i = 0

    string = key
    while not found:

        hash_string = hashlib.md5(string.encode())

        if hex(hash_string[0:5]) == "00000":
            found = True
            break
        
        hash_string = key + str(i)
        i += 1
    
    



result = hashlib.md5('GeeksforGeeks'.encode())
print(result.hexdigest())