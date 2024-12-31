"""Script that contains solutions to day 5 2024."""
def extract_rules(data: str) -> list[list[int]]:
    """Extracts rules of the input."""

    split_data = data.split('\n')

    rules = []
    for line in split_data:
        print(line)
        if '|' in line:
            print('| present')
            rule = line.split('|')
            print(rule)
            print([int(rule[0]),int(rule[1])])
            rules.append([int(rule[0]),int(rule[1])])

    return rules


def extract_sequences(data: str) -> list[list[int]]:
    """Extracts sequences of the input"""

    split_data = data.split('\n')

    sequences = []
    for line in split_data:
        if ',' in line:
            sequence = line.split(',')
            sequences.append([int(num) for num in sequence])

    return sequences


def valid_rule(sequence: list[int], rule: list[int]) -> bool:
    """Returns if a rule is followed by a sequence."""

    for i in range(len(sequence)):

        if sequence[i] == rule[0]:
            return True
        elif sequence[i] == rule[1]:
            return False
    
    return True


def valid_sequence(sequence: list[int], rules: list[list[int]]) -> bool:
    """Returns if a sequence follows the given rules."""

    for rule in rules:
        if rule[0] in sequence and rule[1] in sequence:
            if not valid_rule(sequence, rule):
                return False

    return True


def solve_day_five_pt_one(data) -> int:
    """Returns the sum of the middle numbers of valid sequences."""

    rules = extract_rules(data)
    sequences = extract_sequences(data)

    total_middle = 0

    for sequence in sequences:
        if valid_sequence(sequence, rules):
            total_middle += find_middle(sequence)

    return total_middle



if __name__ == '__main__':

    with open('day_five_input.txt','r',encoding='UTF-8') as file:
        input_data = file.read()

    print(input_data)
    print(extract_rules(input_data))
    print(extract_sequences(input_data))
