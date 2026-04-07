import sys

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

points = []
for line in lines:
    x, y = map(int, line.split(','))
    points.append((x, y))

part1 = 0
for i, (x1, y1) in enumerate(points):
    for j, (x2, y2) in enumerate(points):
        if i < j:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) +1)
            part1 = max(part1, area)
            
print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")