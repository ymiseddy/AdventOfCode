import tools as t
import math
import numpy as np
import re

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    data = []
    for line in lines:
        ss, dd = line.split(":", 1)
        idx = int(ss.split(" ")[1])
        parts = dd.split(",")
        info = {}
        for part in parts:
            k,v = part.split(":")
            info[k.strip()] = int(v)
        data.append((idx, info))
    return data

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)

    match = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    mkeys = set(match.keys())
    print(mkeys)
    for id,d in data:
        dkeys = set(d.keys())
        common = mkeys.intersection(dkeys)
        is_match = True
        for c in common:
            if d[c] != match[c]:
                is_match = False
        if is_match:
            print(f"{id} matches")
            result = id

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    match = {
        "children": 3,
        "samoyeds": 2,
        "akitas": 0,
        "vizslas": 0,
        "cars": 2,
        "perfumes": 1
    }

    greater = {
        "cats": 7,
        "trees": 3
    }
    less = {
        "pomeranians": 3,
        "goldfish": 5
    }

    mkeys = set(match.keys())
    print(mkeys)
    for id,d in data:
        dkeys = set(d.keys())
        common = mkeys.intersection(dkeys)
        is_match = True
        for c in common:
            if d[c] != match[c]:
                is_match = False
        for c,v in greater.items():
            if c in d and d[c] <= v:
                is_match = False

        for c,v in less.items():
            if c in d and d[c] >= v:
                is_match = False

        if is_match:
            print(f"{id} matches")
            result = id
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day16.txt")

    print()

    part_02("day16.txt")

