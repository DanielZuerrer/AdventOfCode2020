from functools import reduce

def move(origin, movement):
    return (origin[0] + movement[0], origin[1] + movement[1])

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

line_length = len(lines[0])
pos = (0,0)
possible_slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def check_slope(slope):
    tree_count = 0
    pos = (0,0)
    while pos[1] < len(lines):
        if lines[pos[1]][pos[0] % (line_length)] =='#':
            tree_count += 1

        pos = move(pos, slope)

    return tree_count

trees = map(check_slope, possible_slopes)

total_trees = reduce(lambda acc, e: acc * e, trees)

print(total_trees)

