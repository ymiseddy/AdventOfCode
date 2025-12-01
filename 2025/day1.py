import tools as t
import numpy as np
from collections import Counter

def load_data(filename):
    data = t.load(filename)
    lines = data.splitlines()
    steps = [(x[0], int(x[1:])) for x in lines]
    return steps

def part_01(filename="2025/day1s1.txt"):
    steps = load_data(filename)
    p = 50
    zcount = 0
    for (direction, count) in steps:
        if direction == "R":
            p = (p + count) % 100
        else:
            p = (p - count) % 100
        if p == 0:
            zcount += 1

    print(f"Part 1: max= {maxr} zero count = {zcount}")

def part_02(filename="2025/day1s1.txt"):
    steps = load_data(filename)
    p = 50
    zcount = 0
    for (direction, count) in steps:
        ztimes = 0
        if direction == "R":
            d = 100 - p
            ztimes = 1 + (count - d) // 100
            p = (p + count) % 100
        else:
            d = p

            # Don't count if we are starting on a zero
            ztimes += 1 * (p != 0) + (count - d) // 100
            p = (p - count) % 100
        zcount += ztimes

    print(f"Part 2: zero count = {zcount}")

if __name__ == "__main__":
    part_01("day1s1.txt")
    part_01("day1.txt")

    print()

    part_02("day1s1.txt")
    part_02("day1.txt")
