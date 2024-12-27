"""File containing solutions to advent of code 2024 day one."""

def reconcile_lists(list_one, list_two):
    """returns the thing"""

    list_one = sorted(list_one)
    list_two = sorted(list_two)
    difference = []

    for i in range(len(list_one)):
        difference.append(abs(int(list_one[i])-int(list_two[i])))

    return sum(difference)

def part_two(list_one, list_two):
    """returns a different thing"""

    dict_count = {}

    for value in list_one:
        dict_count[value] = 0
    
    for value in list_two:
        if value in dict_count.keys():
            dict_count[value] += 1
    
    total = 0

    for value in dict_count:
        total += int(value) * int(dict_count[value])
    
    return total



if __name__ == '__main__':

    with open('day_one_input.txt', 'r', encoding='UTF-8') as file:
        data = file.read()

    list_one = []
    list_two = []

    for values in data.split('\n'):

        list_one.append(values.split()[0])
        list_two.append(values.split()[1])

    print(reconcile_lists(list_one, list_two))
    print(part_two(list_one, list_two))