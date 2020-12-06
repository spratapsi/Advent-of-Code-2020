import itertools as it
import functools as ft

def group_lines(file):
    """Split input file into groups divided by blank lines."""
    clean_lines = (line.strip() for line in file)
    groups = it.groupby(clean_lines, key=bool)
    yield from (lines for is_blank, lines in groups if not is_blank)

def union(sets):
    return ft.reduce(set.union, sets)

def intersection(sets):
    return ft.reduce(set.intersection, sets)

with open('6.in') as file:
    groups = group_lines(file)
    group_answers = [set(line) for line in groups]

part1 = sum(len(union(answers)) for answers in group_answers)
part2 = sum(len(intersection(answers)) for answers in group_answers)

print('Part 1:', part1)
print('Part 1:', part2)
