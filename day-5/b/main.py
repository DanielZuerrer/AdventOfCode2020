with open('input.txt', 'r') as f:
    input = f.read()

binary_input = input.replace('F', '0').replace(
    'B', '1').replace('R', '1').replace('L', '0')

ids = set([int(boarding_pass, base=2)
       for boarding_pass in binary_input.split('\n')[:-1]])

all_seats = set(range(min(ids), max(ids)+1))

print(all_seats - ids)
