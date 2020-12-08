with open('input.txt', 'r') as f:
    input = f.read()

double_space_separated = input.replace('\n', ' ')
passports = double_space_separated.split('  ')

necessary_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def is_valid(passport):
    is_valid = True
    for field in necessary_fields:
        is_valid &= f'{field}:' in passport

    return is_valid


passport_validities = map(is_valid, passports)

number_of_valid_passports = len(list(filter(lambda x: x, passport_validities)))

print(number_of_valid_passports)
