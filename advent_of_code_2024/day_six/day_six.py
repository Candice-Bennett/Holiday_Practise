"""Script containing all the functions for day six."""

def comprehend_input(grid_string: str) -> list[str]:
    """Takes the grid string and turns it into a list"""
    return grid_string.split('\n')


def locate_item(grid: list[str], item: str) -> list[int]:
    """Takes the grid and returns the coordinate [x,y] where the officer is
    where +x is eastwardly and +y is southern."""
    
    coords = []

    for i in range(len(grid)):
        if item in grid[i]:
            for j in range(len(grid[i])):
                if grid[i][j] == item:
                    coords.append([i,j])
    
    return coords


def part_one_solution(grid_string: str) -> int:
    """Returns the number of spaces visited by the officer."""
    ...

if __name__ == '__main__':

    string = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

    print(string)
    print(comprehend_input(string))
    print(locate_officer(comprehend_input(string)))
