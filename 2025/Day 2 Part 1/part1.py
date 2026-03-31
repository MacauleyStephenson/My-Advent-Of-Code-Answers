import sys

def is_invalid(i: int) -> bool:
    code = str(i)
    if len(code) % 2 != 0:
        return False
    return code[:len(code)//2] == code[len(code) //2:]


with open(sys.argv[1], 'r') as f: 
    ranges = f.read().strip().split(',')


part1 = 0
for r in ranges:
    start, end = map(int, r.split('-'))
    for i in range(start, end +1):
        if is_invalid(i):
            part1 += i
print(f'Part 1: {part1}')

part2 = ""
print(f'Part 2: {part2}')