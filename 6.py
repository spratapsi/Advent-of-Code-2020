import itertools as it
import functools as ft

def group_lines(file):
    """Clean and group lines (divided by blank lines)."""
    clean_lines = (line.strip() for line in file)
    groups = it.groupby(clean_lines, key=bool)
    return (lines for is_not_blank, lines in groups if is_not_blank)

def union(sets):
    return ft.reduce(set.union, sets)

def intersection(sets):
    return ft.reduce(set.intersection, sets)

with open('6.in') as file:
    groups = group_lines(file)
    group_answers = [[set(line) for line in group] for group in groups]

part1 = sum(len(union(answers)) for answers in group_answers)
part2 = sum(len(intersection(answers)) for answers in group_answers)

print('Part 1:', part1)
print('Part 1:', part2)
