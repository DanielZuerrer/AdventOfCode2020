import re

with open('input.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    input = f.read()

double_space_separated = input.replace('\n', ' ')
passports = double_space_separated.split('  ')


def validate_byr(value):
    try:
        byr = int(value)
        return byr >= 1920 and byr <= 2002
    except:
        return False


def validate_iyr(value):
    try:
        iyr = int(value)
        return iyr >= 2010 and iyr <= 2020
    except:
        return False


def validate_eyr(value):
    try:
        eyr = int(value)
        return eyr >= 2020 and eyr <= 2030
    except:
        return False


def validate_hgt(value):
    regex = r"(?P<height>\d+)(?P<unit>in|cm)"
    match = re.match(regex, value)
    if not match:
        return False
    parsed = match.groupdict()
    if not parsed:
        return False
    if parsed['unit'] == 'in':
        height = int(parsed['height'])
        return height >= 59 and height <= 76
    if parsed['unit'] == 'cm':
        height = int(parsed['height'])
        return height >= 150 and height <= 193
    return False


def validate_hcl(value):
    regex = r"^#[\d|[a-f]{6}$"
    matches = re.findall(regex, value)
    return len(matches) == 1


def validate_ecl(value):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value in valid_colors


def validate_pid(value):
    regex = r"^\d{9}$"
    matches = re.findall(regex, value)
    return len(matches) == 1


validations = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid
}

def is_valid(passport):
    for field in validations.keys():
        is_valid = f'{field}:' in passport
        if not is_valid:
            return False

    for field, validator in validations.items():
        regex = rf"{field}:(.+?)(\s|$)"
        match = re.findall(regex, passport)[0][0]
        is_valid = validator(match)
        if not is_valid:
            return False

    return True


passport_validities = map(is_valid, passports)

number_of_valid_passports = len(list(filter(lambda x: x, passport_validities)))

print(number_of_valid_passports)
