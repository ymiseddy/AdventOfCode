import tools as t
import math
import numpy as np
import re

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    total_code = 0
    total_memory = 0
    for line in data:
        total_code += len(line)
        chomped = line[1:-1]
        t = 0
        memory = 0
        while t < len(chomped):
            if chomped[t] == "\\":
                if chomped[t + 1] == "x":
                    t += 4
                else:
                    t += 2
            else:
                t += 1
            total_memory += 1
            memory += 1
        #print(f"{line}: {len(line)}-{memory}")
    result = total_code - total_memory


    print(f"Part 1: total_code:{total_code} total_memory:{total_memory} result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    total_code = 0
    total_encoded = 0
    for line in data:
        total_code += len(line)
        newchars = []
        newchars.append('"')
        for c in line:
            if c == '"' or c == '\\':
                newchars.append("\\")
            newchars.append(c)
        newchars.append('"')
        total_encoded += len(newchars)
        #encoded = "".join(newchars)
        #print(f"{line}:{encoded}:{len(line)}:{len(encoded)}")
    result = total_encoded - total_code
    print(f"Part 2: {total_encoded} {total_code} result = {result}")


if __name__ == "__main__":
    part_01("day8s1.txt")
    part_01("day8.txt")

    print()

    part_02("day8s1.txt")
    part_02("day8.txt")

