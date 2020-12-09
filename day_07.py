import re
from collections import defaultdict

def process_line(line):
    parent, c = line.split(' bags contain ')
    pattern = r'(\d+) (\w+ \w+)'
    matches = [r.groups() for r in re.finditer(pattern, c)]

    if not matches:
        return parent, ()

    children = [(int(n), desc) for n, desc in matches]
    return parent, children

with open('input/day_07.txt') as file:
    tree = dict(process_line(line) for line in file)

inverted_tree = defaultdict(list)
for p, c in tree.items():
    for n, child in c:
        inverted_tree[child].append(p)

def all_children(tree, node):
    """Return all children of node (including repetitions)."""
    for child in tree[node]:
        yield child
        yield from all_children(tree, child)

part1 = len(set(all_children(inverted_tree, 'shiny gold')))

def total_bags(tree, bag):
    return sum(n + n * total_bags(tree, c) for n, c in tree[bag])

part2 = total_bags(tree, 'shiny gold')

print('Part 1:', part1)
print('Part 2:', part2)
