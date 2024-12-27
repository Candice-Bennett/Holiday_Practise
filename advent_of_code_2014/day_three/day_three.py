"""Contains functions to solve advent of code 2014 day three."""

def santa_tracker(string: str) -> int:
    """Returns how many houses santa visited at least once."""

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
    
    #ideally I'd use a map or something to clean the coords_visited array but
    #I don't know the syntax and am writing this on the road
    unique_coords = []
    for co in coords_visited:
        if co not in unique_coords:
            unique_coords.append(co)
    
    return len(unique_coords)

if __name__ == "__main__":

    print(santa_tracker("^>v<"))