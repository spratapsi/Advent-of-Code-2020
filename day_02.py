import re
from dataclasses import dataclass 

@dataclass
class Validate:
    n1: int
    n2: int
    letter: str

    def rule1(self, pwd: str) -> bool:
        count = sum(c == self.letter for c in pwd)
        return self.n1 <= count <= self.n2

    def rule2(self, pwd: str) -> bool:
        s = {pwd[self.n1-1], pwd[self.n2-1]}
        return self.letter in s and len(s) == 2

with open('input/day_02.txt') as file:
    pattern = '(\d+)-(\d+) (\w): (\w+)'
    matches = [re.match(pattern, line).groups() for line in file]
    rules_pwds = [
        (Validate(int(min), int(max), c), pwd)
        for min, max, c, pwd in matches
    ]


part1 = sum(validate.rule1(pwd) for validate, pwd in rules_pwds)
part2 = sum(validate.rule2(pwd) for validate, pwd in rules_pwds)

print('Part 1:', part1)
print('Part 2:', part2)
