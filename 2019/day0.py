import tools as t
import math
import numpy as np
import re

def load_data(filename: str) -> list[int]:
    _data = t.load(filename)
    _lines = data.splitlines()
    return [0]

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day0s1.txt")
    part_01("day0.txt")

    print()

    part_02("day0s1.txt")
    part_02("day0.txt")

