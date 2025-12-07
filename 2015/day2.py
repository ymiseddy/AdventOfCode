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
    gifts = np.array([x.split("x") for x in data]).astype(int)

    for gift in gifts:
        w,h,l = gift
        sides = np.array([l*w, w*h, h*l])
        slack = min(sides)
        wrap = np.sum(2*sides) + slack
        result += wrap
    
    print(f"Part 1: result = {result}")
    return result

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    gifts = np.array([x.split("x") for x in data]).astype(int)
    for gift in gifts:
        min = np.partition(gift, 1)[0:2]
        perimiter = np.sum(2*min)
        volume = np.prod(gift)
        total = perimiter + volume
        result += total
    print(f"Part 2: result = {result}")
    return result


if __name__ == "__main__":
    assert part_01("day2s1.txt") == 101
    assert part_01("day2.txt") == 1598415

    print()

    assert part_02("day2s1.txt") == 48
    assert part_02("day2.txt") == 3812909

