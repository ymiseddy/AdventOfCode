import tools as t
import math
import numpy as np
import re
import typing as ty

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    lines = [int(line) for line in lines]
    return lines


lencount = {}

def dp_1(containers: list, remaining: int, path:list=[]) -> int:
    count = 0
    for idx, c in enumerate(containers):
        new_containers = containers[idx + 1:]
        if c == remaining:
            match = path + [c]
            pathlen = len(match)
            # print(path + [c])
            lencount[pathlen] = lencount.get(pathlen, 0) + 1
            count +=1
        if remaining >= c:
            count += dp_1(new_containers, remaining - c, path + [c])
    return count

def part_01(filename: str, quant: int) -> None:
    result = 0
    lencount = {}
    data = load_data(filename)
    result = dp_1(data, quant)
    print(f"Part 1: result = {result}")

def part_02(filename: str, quant) -> None:
    global lencount
    result = 0
    data = load_data(filename)
    lencount = {}
    result = dp_1(data, quant)

    minlen = min(lencount.keys())
    result = lencount[minlen]

    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day17s1.txt", 25)
    part_01("day17.txt", 150)

    print()

    part_02("day17s1.txt", 25)
    part_02("day17.txt", 150)

