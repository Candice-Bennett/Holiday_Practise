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

if __name__ == '__main__':

    with open('day_five_input.txt','r',encoding='UTF-8') as file:
        input_data = file.read()
    
    print(input_data)
    print(extract_rules(input_data))
    print(extract_sequences(input_data))