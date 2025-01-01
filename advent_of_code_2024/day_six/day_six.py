"""Script containing all the functions for day six."""

def comprehend_input(grid_string: str) -> list[str]:
    """Takes the grid string and turns it into a list"""
    return grid_string.split('\n')


def locate_officer(grid: list[str]) -> list[int]:
    """Takes the grid and returns the coordinate [x,y] where the officer is
    where +x is eastwardly and +y is southern."""
    
    for i in range(len(grid)):
        if '^' in grid[i]:
            for j in range(len(grid[i])):
                if grid[i][j] == '^':
                    return [i,j]
    
    raise ValueError('This input does not contain an officer')


def locate_obstructions(grid: list[str]) -> list[list[int]]:
    """Returns all the grid coordinates of the obstructions."""
    

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
