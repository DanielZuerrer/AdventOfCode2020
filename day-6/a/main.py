with open('input.txt', 'r') as f:
    input = f.read()

double_space_separated = input.replace('\n', ' ')
group_answers = double_space_separated.split('  ')
group_answers = [set(a.replace(' ', '')) for a in group_answers]

yes_answer_count = [len(answers) for answers in group_answers]

print(sum(yes_answer_count))
