import itertools as it
import re

class Passport(dict):
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

    def is_complete(self):
        return self.fields ^ self.keys() <= {'cid'}

    def is_valid(s):
        if not s.is_complete():
            return False

        byr = re.fullmatch(r'\d{4}', s['byr']) and (1920 <= int(s['byr']) <= 2002)
        iyr = re.fullmatch(r'\d{4}', s['iyr']) and (2010 <= int(s['iyr']) <= 2020)
        eyr = re.fullmatch(r'\d{4}', s['eyr']) and (2020 <= int(s['eyr']) <= 2030)
        hgt = re.fullmatch(r'\d+(cm|in)', s['hgt']) and (
            150 <= int(s['hgt'][:-2]) <= 193
            if s['hgt'].endswith('cm')
            else 59 <= int(s['hgt'][:-2]) <= 76
        )
        hcl = re.fullmatch(r'#[0-9a-f]{6}', s['hcl'])
        ecl = s['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        pid = re.fullmatch(r'\d{9}', s['pid'])

        return all([byr, iyr, eyr, hgt, hcl, ecl, pid])

    @classmethod
    def from_record(cls, record: str):
        """Turn strings of type 'key1:val1 key2:val2 ... keyn:valn'
        into Passport objects."""
        key_values = (k_v.split(':') for k_v in record.split(' '))
        p = {k: v for k, v in key_values}
        return cls(p)


def records_from_file(file):
    """Extract records from file and output them as single lines."""

    def split_records(file):
        """Return groups of consecutive non-blank lines."""
        groups = it.groupby(file, key=lambda line: line == '\n')
        return (group for is_blank, group in groups if not is_blank)

    def join_lines(lines):
        return ' '.join(line.strip() for line in lines)

    return (join_lines(record) for record in split_records(file))


with open('4.in') as file:
    records = records_from_file(file)
    passports = [Passport.from_record(r) for r in records]

part1 = sum(passport.is_complete() for passport in passports)
part2 = sum(passport.is_valid() for passport in passports)

print('Part 1:', part1)
print('Part 2:', part2)
