from functools import reduce

with open('input.txt', 'r') as f:
    input = f.read().rstrip('\n')

double_space_separated = input.replace('\n', ' ')
group_answers = double_space_separated.split('  ')

group_answers = [a.split(' ') for a in group_answers]

group_answers = [[set(a) for a in b] for b in group_answers]

group_answers = [reduce(lambda acc, e: acc & e, a) for a in group_answers]

yes_answer_count = [len(answers) for answers in group_answers]

print(sum(yes_answer_count))
