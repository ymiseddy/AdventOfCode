import tools as t
import math
import numpy as np
import re

arrows = {
        "^": np.array([0,-1]),
        ">": np.array([1,0]),
        "v": np.array([0,1]),
        "<": np.array([-1,0]),
}



def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    pos = np.array([0,0])
    visited = {tuple(pos)}
    for line in data:
        for c in line:
            if c not in arrows:
                print("not found!")
                continue
            pos += arrows[c]
            visited.add(tuple(pos))
    result = len(visited)

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    spos = np.array([0,0])
    rpos = np.array([0,0])
    pos = spos;
    visited = {tuple(pos)}
    s = True
    for line in data:
        for c in line:
            if c not in arrows:
                print("not found!")
                continue
            if s:
                spos += arrows[c]
                pos = spos
            else:
                rpos += arrows[c]
                pos = rpos
            s = not s
            visited.add(tuple(pos))
    result = len(visited)

    print(f"Part 1: result = {result}")


if __name__ == "__main__":
    part_01("day3s1.txt")
    part_01("day3.txt")

    print()

    part_02("day3s1.txt")
    part_02("day3.txt")

