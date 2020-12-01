from itertools import combinations

with open('input.txt', 'r') as f:
    entries = set([int(e) for e in f.readlines()])

numbers = list(filter(lambda c: sum(c) == 2020, combinations(entries, 3)))[0]

result = numbers[0] * numbers[1] * numbers[2]

print(result)
