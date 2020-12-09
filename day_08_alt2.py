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

def code_variations(code):
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for i, (inst, arg) in enumerate(code):
        if inst not in swap:
            continue

        new_code = list(code)
        new_inst = swap[inst]
        new_code[i] = (new_inst, arg)
        yield new_code

for code_ in code_variations(code):
    acc, stopped = run(code_)
    if stopped:
        part2 = acc
        break

print('Part 1:', part1)
print('Part 2:', part2)
