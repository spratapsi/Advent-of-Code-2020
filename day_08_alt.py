with open('input/day_08.txt') as file:
    input_code = (line.strip().split(' ') for line in file)
    code = [(inst, int(arg)) for inst, arg in input_code]

def run(code, ptr=0, acc=0):
    visited = set()
    while not (stopped := ptr >= len(code)) and (ptr not in visited):
        visited.add(ptr)
        instr, arg = code[ptr]
        ptr += arg if instr == 'jmp' else 1
        acc += arg if instr == 'acc' else 0

    return acc, stopped

part1, _ = run(code)

class Cycle:
    stops = False

ptr = 0
cycles = {}
cycle = Cycle()
remaining_codes = list(range(len(code)))
while remaining_codes:
    if (out_of_bounds := ptr >= len(code)) or (ptr in cycles):
        cycle.stops = True if out_of_bounds else cycles[ptr].stops
        cycle = Cycle()
        ptr = remaining_codes[0]
    else:
        cycles[ptr] = cycle
        remaining_codes.remove(ptr)

        instr, arg = code[ptr]
        ptr += arg if instr == 'jmp' else 1

ptr = 0
while True:
    instr, arg = code[ptr]
    new_instr = {'acc': 'acc', 'jmp': 'nop', 'nop': 'jmp'}[instr]
    new_ptr = ptr + (arg if new_instr == 'jmp' else 1)
    if new_ptr >= len(code) or cycles[new_ptr].stops:
        new_code = list(code)
        new_code[ptr] = (new_instr, arg)
        break
    else:
        ptr += (arg if instr == 'jmp' else 1)

part2, _ = run(new_code)

print('Part 1:', part1)
print('Part 2:', part2)
