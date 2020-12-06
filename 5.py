with open('5.in') as file:
    bpasses = (line.rstrip() for line in file)
    trans = str.maketrans('FBLR', '0101')
    seat_ids = [int(bpass.translate(trans), base=2) for bpass in bpasses]

part1 = max(seat_ids)

sorted_ids = sorted(seat_ids)
for a, b in enumerate(sorted_ids, sorted_ids[0]):
    if a != b:
        part2 = a
        break

print('Part1:', part1)
print('Part1:', part2)