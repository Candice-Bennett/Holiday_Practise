"""Contains functions to solve advent of code 2014 day three."""

def santa_tracker(string: str) -> list[list[int]]:
    """Returns the coordinates santa visits."""

    coords_visited = [[0,0]]
    coord = [0,0]

    for character in string:

        match character:
            case "^":
                coord[1] += 1
            case ">":
                coord[0] += 1
            case "<":
                coord[0] -= 1
            case "v":
                coord[1] -= 1

        coords_visited.append(coord[:])


def coord_splitter(directions: str) -> list[list[str]]:
    """Takes the directions and splits them into into
    instructions for santa and robo-santa."""
    ...


def unique_coord_count(coords: list[list[int]]) -> int:
    """Takes an input of coordinates and returns the number of unique ones"""
    
    #ideally I'd use a map or something to clean the coords_visited array but
    #I don't know the syntax and am writing this on the road
    unique_coords = []
    for coord in coords:
        if coord not in unique_coords:
            unique_coords.append(coord)

    return len(unique_coords)


def robo_santa_tracker(directions: str) -> int:
    """Takes coordinates and returns the number of houses visited when
    santa and robo-santa are both delivering presents."""
    ...


if __name__ == "__main__":

    with open('day_three_input.txt', 'r', encoding='UTF-8') as file:
        input_data = file.read()

    print(unique_coord_count(santa_tracker(input_data)))