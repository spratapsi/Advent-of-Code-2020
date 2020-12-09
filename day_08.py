from enum import Enum, auto

class State(Enum):
    READY = auto()
    INFINITE_LOOP = auto()
    STOPPED = auto()

class Computer:
    def __init__(self, code):
        self.code = code

        self.state = State.READY
        self.accumulator = 0
        self.ptr = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            inst, arg = self.code[self.ptr]
        except IndexError:
            raise StopIteration

        op = self.operations[inst]
        op(self, arg)
        return (inst, arg)

    def run_to_end(self):
        visited = set()
        for instruction in self:
            if self.ptr in visited:
                self.state = State.INFINITE_LOOP
                break
            visited.add(self.ptr)
        else:
            self.state = State.STOPPED

    def acc(self, arg):
        self.accumulator += arg
        self.ptr += 1

    def jmp(self, arg):
        self.ptr += arg

    def nop(self, arg):
        self.ptr += 1

    operations = {
        'acc': acc,
        'jmp': jmp,
        'nop': nop,
    }


with open('input/day_08.txt') as file:
    input_code = (line.strip().split(' ') for line in file)
    code = [(inst, int(arg)) for inst, arg in input_code]

computer = Computer(code)
computer.run_to_end()
part1 = computer.accumulator

def code_variations(code):
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for i, (inst, arg) in enumerate(code):
        if inst not in swap:
            continue

        new_code = list(code)
        new_inst = swap[inst]
        new_code[i] = (new_inst, arg)
        yield new_code

def find_stopping_computer(code):
    for code_ in code_variations(code):
        computer = Computer(code_)
        computer.run_to_end()
        if computer.state is State.STOPPED:
            return computer

part2 = find_stopping_computer(code).accumulator

print('Part 1:', part1)
print('Part 2:', part2)
