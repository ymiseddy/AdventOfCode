from typing import final
import tools as t

@final
class IntCode:

    def __init__(self, code: list[int]=[99], debug:bool=False):
        self.static = code.copy()
        self.code = code.copy()
        self.debug = debug
        self.pc = 0
        self.last_output = None

    def load(self, filename: str) -> None:
        data = t.load(filename)
        nums = data.split(",")
        lines = [int(n) for n in nums]
        self.static = lines
        self.code = lines.copy()

    def peek(self, loc: int) -> int:
        if loc >= len(self.code):
            raise ValueError("Outside of scope.")
        return self.code[loc]

    def step(self):
        op = self.__read()
    
        pmode1 = (op // 100) % 10
        pmode2 = (op // 1000) % 10
        pmode3 = (op // 10000) % 10

        op = op % 100

        if self.debug:
            print(f"op={op} pc={self.pc} pm={pmode1}:{pmode2}:{pmode3}")

        if op == 99:
            if self.debug:
                print("   halt")
            return False

        if op == 1:
            x = self.__read_mode(pmode1)
            y = self.__read_mode(pmode2)
            d = self.__read()
            if self.debug:
                print(f"   add x={x}, y={y}, d={d} pc={self.pc}")
            self.code[d] = x + y
        elif op == 2:
            x = self.__read_mode(pmode1)
            y = self.__read_mode(pmode2)
            d = self.__read()
            if self.debug:
                print(f"   mul x={x}, y={y}, d={d} pc={self.pc}")
            self.code[d] = x * y
        elif op == 3:
            d = self.__read()
            inp = input("   Input integer: ")
            val = int(inp)
            if self.debug:
                print(f"   inp d={d} val={val} pc={self.pc}")
            self.code[d] = val
        elif op == 4:
            x = self.__read_mode(pmode1)
            if self.debug:
                print(f"   out x={x} pc={self.pc}")
            self.last_output = x
            print(f"   Output: {x}")
        elif op == 5:
            x = self.__read_mode(pmode1)
            y = self.__read_mode(pmode2)
            if self.debug:
                print(f"   jmp-true x={x}, y={y} pc={self.pc}")
            if x != 0:
                self.pc = y
        elif op == 6:
            x = self.__read_mode(pmode1)
            y = self.__read_mode(pmode2)
            if self.debug:
                print(f"   jmp-false x={x}, y={y} pc={self.pc}")
            if x == 0:
                self.pc = y
        elif op == 7:
            x = self.__read_mode(pmode1)
            y = self.__read_mode(pmode2)
            d = self.__read()
            res = x < y
            if self.debug:
                print(f"   less-than x={x}, y={y} d={d} pc={self.pc} res={res}")
            if res:
                self.code[d] = 1
            else:
                self.code[d] = 0
        elif op == 8:
            x = self.__read_mode(pmode1)
            y = self.__read_mode(pmode2)
            d = self.__read()
            res = x == y
            if self.debug:
                print(f"   equal x={x}, y={y} d={d} pc={self.pc} res={res}")
            if res:
                self.code[d] = 1
            else:
                self.code[d] = 0

        else:
            raise ValueError(f"Unknown opcode {op} at pc={self.pc}")

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

    def __read_mode(self, mode: int) -> int:
        if mode == 0:
            return self.__read_ind()
        elif mode == 1:
            return self.__read()
        else:
            raise ValueError(f"Unknown parameter mode {mode} at pc={self.pc}")

    def __read(self) -> int:
        assert self.pc < len(self.code)
        d = self.code[self.pc]
        self.pc += 1
        return d

    def __read_ind(self) -> int:
        idx = self.__read()
        assert idx < len(self.code)
        return self.code[idx]


