"""Script that contains solutions to day 5 2024."""
def extract_rules(data: str) -> list[list[int]]:
    """Extracts rules of the input."""

    split_data = data.split('\n')

    rules = []
    for line in split_data:
        if '|' in line:
            rule = line.split('|')
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

        if sequence[i] == rule[1]:
            return False

    return True


def correct_sequence(sequence: list[int], rule: list[int]) -> list[int]:
    """Takes a sequence and corrects it according to the rule."""

    if rule[0] in sequence and rule[1] in sequence and not valid_rule(sequence, rule):

        for i in range(len(sequence)):

            if sequence[i] == rule[1]:
                sequence[i] = rule[0]

            elif sequence[i] == rule[0]:
                sequence[i] = rule [1]

    return sequence
#first just swap any two numbers that break the rule
#if that doesnt work then once recalibrated, rerun whole sequence through rules *again*
#if not generate 'master sequence' then loop through it and pull values as appear from there

def valid_sequence(sequence: list[int], rules: list[list[int]], pt_two=False) -> bool:
    """Returns if a sequence follows the given rules."""

    corrected = False

    for rule in rules:
        if rule[0] in sequence and rule[1] in sequence:
            if not valid_rule(sequence, rule):
                if not pt_two:
                    return False, None
                else:
                    corrected = True
                    sequence = correct_sequence(sequence, rule)

    if not pt_two:
        return True, None

    if pt_two and corrected:
        return True, sequence

    return None, None


def find_middle(sequence: list[int]) -> int:
    """Returns the middle number of the sequence"""

    return sequence[int(len(sequence)/2 - 0.5)]


def solve_day_five_pt_one(data) -> int:
    """Returns the sum of the middle numbers of valid sequences."""

    rules = extract_rules(data)
    sequences = extract_sequences(data)

    total_middle = 0

    for sequence in sequences:
        if valid_sequence(sequence, rules):
            total_middle += find_middle(sequence)

    return total_middle


def solve_day_five_pt_two(data) -> int:
    """Returns the sum of the middle numbers of fixed invalid sequences."""

    rules = extract_rules(data)
    sequences = extract_sequences(data)

    total_middle = 0
    corrected_sequences = []

    for sequence in sequences:

        corrected_sequence = valid_sequence(sequence, rules, True)

        if corrected_sequence[0]:
            print(sequence)
            corrected_sequences.append(corrected_sequence[1])

    print(corrected_sequences)

    for i in range(len(corrected_sequences)):
        for rule in rules:
            corrected_sequences[i] = correct_sequence(corrected_sequences[i], rule)

    print(corrected_sequences)

    for i in range(len(corrected_sequences)):
        for rule in rules:
            corrected_sequences[i] = correct_sequence(corrected_sequences[i], rule)

    print(corrected_sequences)

    for sequence in corrected_sequences:
        total_middle += find_middle(sequence)

    return total_middle


if __name__ == '__main__':

    with open('day_five_input.txt','r',encoding='UTF-8') as file:
        input_data = file.read()

    print(solve_day_five_pt_one(input_data))
