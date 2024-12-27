"""Script contains functions for day two."""

def part_one(numbers):
    """Finds part one answer."""

    list_of_num = numbers.split()
    ascending = False

    if list_of_num[0] < list_of_num[1]:
            ascending = True

    for i in range(len(list_of_num)-1):

        if ascending:

            if not (list_of_num[i] < list_of_num[i+1] <= list_of_num[i] + 3):
                 return False

        else:

            if not (list_of_num[i] > list_of_num[i+1] >= list_of_num[i] - 3):
                 return False
    
    return True

