import sys


def count_paths(start: str, end: str) -> int:
      if start == end:
            return 1
    
      return sum(count_paths(n, end) for n in node_map[start])

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

node_map = {}
for line in lines:
        node, *outs = line.split()
        node_map[node.strip(':')] = outs

part1 = count_paths('you', 'out')
print(f"Part 1: {part1}")

part2 = ""
print(f"Part 2: {part2}")