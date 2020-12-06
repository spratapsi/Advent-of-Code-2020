from itertools import combinations as combs
from functools import reduce
from operator import mul

def prod(numbers):
    return reduce(mul, numbers, 1)

def first(iterable):
    return next(iter(iterable))

with open('1.in') as f:
    report = [int(n) for n in f]

part1 = first(prod(nums) for nums in combs(report, 2) if sum(nums) == 2020)
part2 = first(prod(nums) for nums in combs(report, 3) if sum(nums) == 2020)

print('Part 1:', part1)
print('Part 2:', part2)