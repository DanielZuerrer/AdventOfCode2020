import re

with open('input.txt', 'r') as f:
    input = f.readlines()

regex = r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)"

parsed = [re.match(regex, i).groupdict() for i in input]

def is_valid(password_entry):
    letter_count = password_entry['password'].count(password_entry['letter'])
    return letter_count >= int(password_entry['min']) and letter_count <= int(password_entry['max'])

valid_passwords = list(filter(is_valid, parsed))

print(len(valid_passwords))