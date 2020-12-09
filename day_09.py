import itertools as it
import collections

with open('input/day_09.txt') as file:
    numbers = [int(line) for line in file]

def find_wrong(numbers):
    preamble = collections.deque(numbers[:25])
    for n in numbers[25:]:
        is_valid = any(x + y == n for x, y in it.combinations(preamble, 2))
        if not is_valid:
            return n
        preamble.popleft()
        preamble.append(n)

part1 = find_wrong(numbers)

integral = it.accumulate(numbers)
for (i, ai), (j, aj) in it.combinations(enumerate(integral), 2):
    if part1 == aj - ai:
        break

rng = numbers[i+1:j+1]
part2 = min(rng) + max(rng)

print('Part 1:', part1)
print('Part 2:', part2)