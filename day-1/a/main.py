with open('input.txt', 'r') as f:
    entries = set([int(e) for e in f.readlines()])

differences = set([2020 - e for e in entries])

numbers = list(entries & differences)

result = numbers[0] * numbers[1]

print(result)