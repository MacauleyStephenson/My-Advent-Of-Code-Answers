import sys


with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

part1 = 0

for line in lines:
    nums = [int(c) for c in line]
    first = max(nums[:-1])
    second = max(nums[nums.index(first)+1:])
    part1 += int(f"{first}{second}")

print(f'Part 1: {part1}')

part2 = ""
print(f'Part 2: {part2}')