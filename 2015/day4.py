import tools as t
import math
import numpy as np
import re
import hashlib

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    prefix = "00000"
    for line in data:
        x = 0
        while True:
            x += 1
            h = hashlib.md5(f"{line}{x}".encode()).hexdigest()
            if h.startswith(prefix):
                result = x
                break
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    prefix = "000000"
    for line in data:
        x = 0
        while True:
            x += 1
            h = hashlib.md5(f"{line}{x}".encode()).hexdigest()
            if h.startswith(prefix):
                result = x
                break
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day4s1.txt")
    part_01("day4.txt")

    print()

    part_02("day4s1.txt")
    part_02("day4.txt")

