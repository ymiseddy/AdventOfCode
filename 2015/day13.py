import tools as t
import itertools as it
import math
import numpy as np
import re


parseRe = re.compile("(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).")

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    result = []
    for idx,line in enumerate(lines):
        m = parseRe.match(line)
        if not m:
            raise ValueError(f"Line {idx} did not match.")
        p1, dir, units, p2 = m.groups()
        units = int(units) if dir == "gain" else -int(units)
        result.append((p1, p2, units))
    return result


def max_enjoyment(data):
    costs = {}
    seats = set()
    for s,d,c in data:
        seats.add(s)
        seats.add(d)
        costs[(s,d)] = c
        if (d,s) in costs:
            costs[(d,s)] += c
            costs[(s,d)] = costs[(d,s)]

    seats = list(seats)
    max_enj = 0
    count = len(seats)
    for perm in it.permutations(seats):
        enj = 0
        for idx, person in enumerate(perm):
            next_idx = (idx + 1) % count
            neighbor = perm[next_idx]
            assert person != neighbor
            enj += costs[(person, neighbor)]
            max_enj = max(max_enj, enj)

    return max_enj

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    result = max_enjoyment(data)
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    seats = set()
    for s,d,c in data:
        seats.add(s)

    for x in seats:
        data.append(("Me", x, 0))
        data.append((x, "Me", 0))

    result = max_enjoyment(data)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day13s1.txt")
    part_01("day13.txt")

    print()

    part_02("day13s1.txt")
    part_02("day13.txt")

