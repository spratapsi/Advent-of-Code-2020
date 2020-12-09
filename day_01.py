import itertools as it

with open('input/day_01.txt') as f:
    report = [int(n) for n in f]

# Part 1
for m, n in it.combinations(report, 2):
    if m + n == 2020:
        product1 = m * n
        break

# Part 2
for m, n, p in it.combinations(report, 3):
    if m + n + p == 2020:
        product2 = m * n * p
        break

print('Part 1:', product1)
print('Part 2:', product2)