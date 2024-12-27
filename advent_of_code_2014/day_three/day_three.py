"""Contains functions to solve advent of code 2014 day three."""

def santa_tracker(string: str) -> int:
    """Returns how many houses santa visited at least once."""

    coords_visited = [(0,0)]
    coord = (0,0)

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

        coords_visited.append(coord)
        