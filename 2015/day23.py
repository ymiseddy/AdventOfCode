import tools as t
import re
from dataclasses import dataclass
from typing import override

@dataclass
class Instruction:
    opcode: str
    register: str 
    offset: int 

parseRe = re.compile(r"^(\w{3})\s+([ab])?,?\s*([+-]?\d+)?$")


def load_data(filename: str) -> list[Instruction]:
    data = t.load(filename)
    lines = data.splitlines()
    instructions: list[Instruction] = []
    for line in lines:
        match = parseRe.match(line)
        if not match:
            raise ValueError(f"Line does not match: {line}")

        groups = match.groups()
        op = groups[0]
        reg = "z"
        offset = 0
        if groups[1] in ('a', 'b'):
            reg = groups[1]
        elif groups[1] is not None and groups[1][0] in ('+', '-'):
            offset = int(groups[1])

        if groups[2] is not None:
            offset = int(groups[2])

        instr = Instruction(opcode=op, register=reg, offset=offset)
        instructions.append(instr)

    return instructions

class CPU:
    def __init__(self, instructions: list[Instruction]) -> None:
        self.registers: dict[str, int] = {'a': 0, 'b': 0}
        self._pc: int = 0
        self.instructions: list[Instruction] = instructions

    def step(self) -> None:
        instr = self.instructions[self.pc]
        if instr.opcode == 'hlf':
             self._hlf(instr.register)
        elif instr.opcode == 'tpl':
             self._tpl(instr.register)
        elif instr.opcode == 'inc':
             self._inc(instr.register)
        elif instr.opcode == 'jmp':
             self._jmp(instr.offset)
        elif instr.opcode == 'jie':
             self._jie(instr.register, instr.offset)
        elif instr.opcode == 'jio':
             self._jio(instr.register, instr.offset)
        else:
             raise ValueError(f"Unknown opcode: {instr.opcode}")
        self._pc += 1

        #print(f"{instr.opcode} {instr.register} {instr.offset} => PC: {self._pc}, Registers: {self.registers}")

    @property
    def a(self) -> int:
        return self.registers['a']

    @a.setter
    def a(self, value: int) -> None:
        self.registers['a'] = value

    @property
    def b(self) -> int:
        return self.registers['b']

    @b.setter
    def b(self, value: int) -> None:
        self.registers['b'] = value

    @property
    def pc(self) -> int:
        return self._pc

    @pc.setter
    def set_pc(self, value: int) -> None:
        self._pc = value

    def reset(self) -> None:
        self.registers = {'a': 0, 'b': 0}
        self._pc = 0

    def run(self) -> None:
        while 0 <= self._pc < len(self.instructions):
            self.step()

    @override
    def __repr__(self) -> str:
        return f"PC: {self._pc}, Registers: {self.registers}"


    def _hlf(self, reg: str) -> None:
        self.registers[reg] //= 2

    def _tpl(self, reg: str) -> None:
        self.registers[reg] *= 3

    def _inc(self, reg: str) -> None:
        self.registers[reg] += 1

    def _jmp(self, offset: int) -> None:
        self._pc += offset - 1

    def _jie(self, reg: str, offset: int) -> None:
        if self.registers[reg] % 2 == 0:
            self._pc += offset - 1

    def _jio(self, reg: str, offset: int) -> None:
        if self.registers[reg] == 1:
            self._pc += offset - 1


def list_instructions(instructions: list[Instruction]) -> None:
    for i, instr in enumerate(instructions):
        print(f"{i:03}: {instr.opcode} {instr.register if instr.register != "z" else ''} {instr.offset if instr.offset != 0 else ''}")

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    #list_instructions(data)
    cpu = CPU(data)
    cpu.run()
    print(cpu)
    result = cpu.b
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    cpu = CPU(data)
    cpu.a = 1
    cpu.run()
    print(cpu)
    result = cpu.b
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day23s1.txt")
    part_01("day23.txt")

    print()

    #part_02("day23s1.txt")
    part_02("day23.txt")

