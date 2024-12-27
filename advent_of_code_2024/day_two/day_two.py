"""Script contains functions for day two."""

def part_one(list_of_num):
    """Finds part one answer."""

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

if __name__ == '__main__':

    total = 0

    with open('day_two_input.txt', 'r', encoding='UTF-8') as file:
        input_data = file.read()

    input_data = input_data.split('\n')

    for puzzle in input_data:
        num_list = puzzle.split(' ')

        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])

        if part_one(num_list):
            total += 1
    
    print(total)
