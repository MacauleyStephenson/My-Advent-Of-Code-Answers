import sys
import math

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

operators = lines[-1].split() #Python can split the chunks without any input
num_rows = [list(map(int, line.split())) for line in lines [:-1]]


part1 = 0
for nums, op in zip(zip(*num_rows), operators):#takes the first item and puts it together + second item and so on
    if op == "+":
        part1 += sum(nums)
    elif op == "*":
        part1 += math.prod(nums) 
    else:    
        raise

print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")
