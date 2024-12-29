import re

if __name__ == "__main__":

    with open('day_three_input.txt','r',encoding='UTF-8') as file:
        input_data = file.read()

    regex = re.compile(r'mul\(\d\d?\d?,\d\d?\d?\)')
    valid_code = regex.findall(input_data)
    print(valid_code)

