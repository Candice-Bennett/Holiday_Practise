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


def move_officer(officer_location: list[int],
                obstruction_locations: list[list[int]],
                boundaries: list[int],
                direction: int) -> tuple[list[int], bool]:
    """Returns all the coordinates covered in the move"""

    stopping_object = [None, None]

    match direction:

        case 1: #go north
            for obstruction in obstruction_locations:
                if obstruction[1] == officer_location[1]:
                    if obstruction[0] < officer_location[0] and obstruction[0] > stopping_object[0]:
                        stopping_object = obstruction
            
            coords_traveled = [officer_location]

            if stopping_object != [None, None]:
                left_grid = False
                for i in range(abs(officer_location[0]-stopping_object[0])):
                    coords_traveled.append([officer_location[0]-i,officer_location[1]])
            
            else:

                left_grid = True
                for i in range(officer_location[1]):
                    coords_traveled.append([officer_location[0]-i,officer_location[1]]) 

            return (coords_traveled, left_grid)

        case 2: #go east
            for obstruction in obstruction_locations:
                if obstruction[0] == officer_location[0]:
                    if obstruction[1] > officer_location[1] and obstruction[1] > stopping_object[1]:
                        stopping_object = obstruction
            
            coords_traveled = [officer_location]

            if stopping_object != [None, None]:
                left_grid = False
                for i in range(abs(officer_location[1]-stopping_object[1])):
                    coords_traveled.append([officer_location[0],officer_location[1]+i])
            
            else:

                left_grid = True
                for i in range(abs(officer_location[1]-boundaries[1])):
                    coords_traveled.append([officer_location[0],officer_location[1]+i]) 

            return (coords_traveled, left_grid)

        case 3: #go south
            for obstruction in obstruction_locations:
                if obstruction[1] == officer_location[1]:
                    if obstruction[0] > officer_location[0] and obstruction[0] < stopping_object[0]:
                        stopping_object = obstruction
            
            coords_traveled = [officer_location]

            if stopping_object != [None, None]:
                left_grid = False
                for i in range(abs(officer_location[0]-stopping_object[0])):
                    coords_traveled.append([officer_location[0]+i,officer_location[1]])
            
            else:
                left_grid = True
                for i in range(abs(officer_location[1]-boundaries[0])):
                    coords_traveled.append([officer_location[0]+i,officer_location[1]]) 

            return (coords_traveled, left_grid)

        case 4: #go west
            for obstruction in obstruction_locations:
                if obstruction[0] == officer_location[0]:
                    if obstruction[1] < officer_location[1] and obstruction[1] < stopping_object[1]:
                        stopping_object = obstruction
            
            coords_traveled = [officer_location]

            if stopping_object != [None, None]:
                left_grid = False
                for i in range(abs(officer_location[1]-stopping_object[1])):
                    coords_traveled.append([officer_location[0],officer_location[1]-i])
            
            else:

                left_grid = True
                for i in range(officer_location[1]):
                    coords_traveled.append([officer_location[0],officer_location[1]-i]) 

            return (coords_traveled, left_grid)


def part_one_solution(grid_string: str) -> int:
    """Returns the number of spaces visited by the officer."""
    
    grid = comprehend_input(grid_string)

    officer_coords = locate_item(grid,'^')[0]
    obstruction_coords = locate_item(grid,'#')

    boundaries = [len(grid) - 1,len(grid[0]) - 1]
    inside_grid = True

    officer_direction = 1

    total_coords = []

    while inside_grid:
        coords_moved = move_officer(officer_coords, obstruction_coords,
                                    officer_direction, boundaries)

        officer_coords = coords_moved[0][-1]

        for coord in coords_moved[0]:

            if not coord in total_coords:
                total_coords.append(coord)
        
        officer_direction == (officer_direction % 4) + 1
        inside_grid = coords_moved[1]
    
    return len(total_coords)


if __name__ == '__main__':

    print([(i % 4) + 1 for i in range(12)])
