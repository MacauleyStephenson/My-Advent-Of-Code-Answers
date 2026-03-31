import sys

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

part1 = 0
pos = 50

for line in lines:
    val = int(line.replace('L', '-').replace('R', ''))
    pos = (pos + val) % 100
    if pos == 0:
        part1 += 1
print(f'Part 1: {part1}')

part2 = ""
print(f'Part 2: {part2}')