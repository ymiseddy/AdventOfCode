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
    for line in data:
        result = sum([1 if x == '(' else -1 for x in line])
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for line in data:
        floor = 0
        for i, c in enumerate(line):
            floor += 1 if c == '(' else -1
            if floor == -1:
                result = i + 1
                break
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day1s1.txt")
    part_01("day1.txt")

    print()

    part_02("day1s1.txt")
    part_02("day1.txt")

