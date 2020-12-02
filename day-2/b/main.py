import re

with open('input.txt', 'r') as f:
    input = f.readlines()

regex = r"(?P<pos_1>\d+)-(?P<pos_2>\d+) (?P<letter>\w): (?P<password>\w+)"

parsed = [re.match(regex, i).groupdict() for i in input]

def is_valid(password_entry):
    pos_1_match = password_entry['password'][int(password_entry['pos_1'])-1] == password_entry['letter']
    pos_2_match = password_entry['password'][int(password_entry['pos_2'])-1] == password_entry['letter']

    return pos_1_match != pos_2_match

valid_passwords = list(filter(is_valid, parsed))

print(len(valid_passwords))