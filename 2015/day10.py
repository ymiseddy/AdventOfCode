import tools as t
import math
import numpy as np
import re

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines[0]

def look_and_say(sequence: str) -> str:
    result = []
    count = 1
    c = sequence[0]
    for char in sequence[1:]:
        if char != c:
            result.append(str(count))
            result.append(c)
            c = char
            count = 1
        else:
            count += 1
    result.append(str(count))
    result.append(c)
    return "".join(result)

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    count = 50
    sequence = data
    for i in range(count):
        sequence = look_and_say(sequence)
        print(f"After {i+1} iterations: length = {len(sequence)}")
    result = len(sequence)

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day10s1.txt")
    part_01("day10.txt")

    print()

    #part_02("day10s1.txt")
    #part_02("day10.txt")

