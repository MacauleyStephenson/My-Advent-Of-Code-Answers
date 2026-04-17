import sys
from itertools import combinations

def find_min_pushes(target, buttons):
    for i in range(1, len(buttons) + 1):
        for comb in combinations(buttons, i):
            result = 0
            for c in comb:
                result ^= c
            if result == target:
                return i

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

part1 = 0
for line in lines:
    target_s, *buttons_s, power_s = line.split()
    target = int(target_s.strip('[]')[::-1].replace('#', '1').replace('.', '0'), 2)    
    buttons = [sum(pow(2, int(b)) for b in button.strip('()').split(',')) for button in buttons_s]

    part1 += find_min_pushes(target, buttons)
print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")