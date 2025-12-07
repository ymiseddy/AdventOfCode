import tools as t
import math
import numpy as np
import re

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    parts = []
    for line in lines:
        operation, target = line.split("->")
        operation = operation.strip()
        target = target.strip()
        operation = operation.split(" ")
        parts.append([operation, target])

    return parts

reReg = re.compile(r"^[a-z]+$")
reNumber = re.compile(r"[0-9]+$")

def get_value(v: str, registers: dict)-> np.uint32 | None:
    res = None
    if reReg.match(v):
        if v in registers:
            res = registers[v]
    elif reNumber.match(v):
        res = np.uint16(v)
    else:
        raise f"Invalid value: {v}"
    return res


def evaluate(op: list, registers: dict)-> np.uint32 | None:
    if len(op) == 1:
        return get_value(op[0], registers)
    if len(op) == 2:
        gate, val = op
        if gate != 'NOT':
            raise f"Invalid gate: {gate}"
        if (rval := get_value(val, registers)) != None:
            return ~rval
        return None
    if len(op) == 3:
        lval, gate, rval = op

        if (lval := get_value(lval, registers)) == None:
            return None

        if (rval := get_value(rval, registers)) == None:
            return None

        if gate == 'AND':
            return lval & rval
        if gate == 'OR':
            return lval | rval
        if gate == 'LSHIFT':
            return lval << rval
        if gate == 'RSHIFT':
            return lval >> rval

        raise f"Invalid gate: {gate}"

    raise "Invalid operation"

def run(log: list, registers: dict):
    while True:
        newlog = []
        for op, target in log:
            if (val := evaluate(op, registers)) != None:
                registers[target] = val
            else:
                newlog.append([op, target])
        if len(newlog) == 0:
            break
        log = newlog

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    registers = {}
    run(data, registers)
    result = registers.get("a", None)
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    registers = {}
    run(data, registers)

    # Hard coding the override here. 
    a = f"{registers['a']}"
    data[3][0][0] = a
    registers = {}

    run(data, registers)

    result = registers["a"]
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day7.txt")

    print()

    part_02("day7.txt")

