"""File containing solutions to advent of code 2024 day one."""

def reconcile_lists(list_one, list_two):
    list_one = sorted(list_one)
    list_two = sorted(list_two)
    difference = []

    for i in range(len(list_one)):
        difference.append(abs(int(list_one[i])-int(list_two[i])))

    return sum(difference)

if __name__ == '__main__':

    with open('day_one_input.txt', 'r', encoding='UTF-8') as file:
        data = file.read()

    list_one = []
    list_two = []

    for values in data.split('\n'):

        list_one.append(values.split()[0])
        list_two.append(values.split()[1])

    print(reconcile_lists(list_one, list_two))