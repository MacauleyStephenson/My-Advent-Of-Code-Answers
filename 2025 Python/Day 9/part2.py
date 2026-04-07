import sys

def point_in_poly(x: int, y: int) -> bool:
    inside = False

    for (x1, y1,), (x2, y2) in zip(points, points[1:] + points[:1]):
        if (x == x1 == x2 and min(y1, y2) <= y <= max(y1, y2) or
            y == y1 == y2 and min(x1, x2) <= x <= max(x1, x2)):
            return True
        #assert (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2)
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) +x1):
            inside = not inside
        
        return inside
    
def square_valid(x1, x2, y1, y2):
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if not point_in_poly(x, y):
                return False
    
    return True

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

points = []
for line in lines:
    x, y = map(int, line.split(','))
    points.append((x, y))

part1 = 0
part2 = 0
for i, (x1, y1) in enumerate(points):
    for j, (x2, y2) in enumerate(points):
        if i < j:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) +1)
            part1 = max(part1, area)
            if area > part2 and square_valid(x1, x2, y1, y2):
                part2 = area
            
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")