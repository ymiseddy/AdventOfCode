import tools as t
import math
import numpy as np
import re
from typing import final

@final
class IntCode:
    
    def __init__(self, code: list[int],debug=False):
        self.static = code.copy()
        self.code = code.copy()
        self.debug = debug
        self.pc = 0

    def __read(self, n: int=0) -> int:
        return self.code[self.pc + n]

    def __read_ind(self, n: int) -> int:
        idx = self.__read(n)
        return self.code[idx]

    def peek(self, loc: int) -> int:
        if loc >= len(self.code):
            raise ValueError("Outside of scope.")
        return self.code[loc]

    def step(self):
        op = self.__read()
        if op == 99:
            return False

        if op == 1:
            x = self.__read_ind(1)
            y = self.__read_ind(2)
            d = self.__read(3)
            if self.debug:
                print(f"add x={x}, y={y}, d={d} pc={self.pc}")
            self.code[d] = x + y

        if op == 2:
            x = self.__read_ind(1)
            y = self.__read_ind(2)
            d = self.__read(3)
            if self.debug:
                print(f"mul x={x}, y={y}, d={d} pc={self.pc}")
            self.code[d] = x * y

        self.pc += 4
        return True

    def run(self, noun:int | None = None, verb: int | None = None):
        self.pc = 0
        self.code = self.static.copy()
        if noun is not None:
            self.code[1] = noun
        if verb is not None:
            self.code[2] = verb

        while(self.step()):
            pass



def load_data(filename: str) -> list[int]:
    data = t.load(filename)
    nums = data.split(",")
    lines = [int(n) for n in nums]
    return lines

def part_01(filename: str, noun:int|None=None, verb:int|None =None) -> None:
    result = 0
    data = load_data(filename)
    comp = IntCode(data)
    comp.run(noun, verb)
    result = comp.peek(0)
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    comp = IntCode(data)
    for noun in range(100):
        for verb in range(100):
            comp.run(noun, verb)
            answer = comp.peek(0)
            print(f"Trying {noun} {verb}: {answer}")
            if answer == 19690720:
                result = 100*noun + verb

    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day02s1.txt")
    part_01("day02.txt", 12,2)

    print()

    #part_02("day02s1.txt")
    part_02("day02.txt")

