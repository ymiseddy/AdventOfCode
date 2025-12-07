import tools as t
import math
import numpy as np
import re

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

def part_01(filename: str) -> float:
    result = 0
    data = load_data(filename)
    data = [list(x) for x in data]
    beams = set()
    x = data[0].index("S")
    beams.add(x)
    assert x != -1

    for line in data[1:]:
        splitters = [i for i,c in enumerate(line) if c == '^']
        for splitter in splitters:
            if splitter not in beams:
                continue
            beams.remove(splitter)
            beams.add(splitter-1)
            beams.add(splitter+1)
            result += 1

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    x = data[0].index("S")
    assert x != -1

    # Note, tried to keep an array of beams but it got too large.
    # Instead, we use a dict to keep track of the counts of each
    # beam position.

    beams = {} 
    beams[x] = 1

    for line in data[1:]:
        splitters = [i for i,c in enumerate(line) if c == '^']
        for splitter in splitters:
            if splitter not in beams:
                continue

            # Update the counts - adding to existing counts if needed
            if splitter-1 in beams:
                beams[splitter-1] += beams[splitter]
            else:
                beams[splitter-1] = beams[splitter]

            if splitter+1 in beams:
                beams[splitter+1] += beams[splitter]
            else:
                beams[splitter+1] = beams[splitter]

            # Remove the original beam.
            beams.pop(splitter)
    result = sum(beams.values())
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day7s1.txt")
    part_01("day7.txt")

    print()

    part_02("day7s1.txt")
    part_02("day7.txt")

