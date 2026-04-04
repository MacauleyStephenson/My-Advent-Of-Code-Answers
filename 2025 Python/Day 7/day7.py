import sys


with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

beams = [lines[0].index('S')]
part1 = 0 

for line in lines[1:]:
    next_beams = set()
    for beam in beams:
        if line[beam] == ".":
            next_beams.add(beam)
        elif line[beam] == "^":
            next_beams.add(beam - 1)
            next_beams.add(beam + 1)
            part1 += 1
    beams = next_beams

print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")