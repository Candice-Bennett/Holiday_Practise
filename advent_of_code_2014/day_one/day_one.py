"""File containing solutions to advent of code 2014 day one."""

def elevators(string: str) -> int:
    """Takes a string and returns the floor number"""

    floor_number = 0

    for character in string:
        if character == "(":

            floor_number += 1

        if character == ")":
            floor_number -= 1

    return floor_number


#I could add a boolean input to the above function but I think there are benefits to keeping them
#Separate adding the boolean would make the code DRY-er as the second function can be built out
#The first, keeping them separate keeps their purposes clearer.
def basement_position(string: str) -> int:
    """Takes a string and returns the position of the character that equates to the basement."""

    floor_number = 0

    for i in range(len(string)):
        if string[i] == "(":

            floor_number += 1

        if string[i] == ")":
            floor_number -= 1

        if floor_number == -1:
            return i + 1

    raise ValueError('This string does not go to the basement!')

if __name__ == "__main__":

    with open('day_one_input.txt', 'r', encoding='UTF-8') as file:
        santa_input = file.read()

    print(elevators(santa_input))
    print(basement_position(santa_input))
