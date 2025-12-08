import tools as t
import math
import numpy as np
import re

pathCostRe = re.compile(r'(\w+) to (\w+) = (\d+)')

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()

    lines = [pathCostRe.match(line).groups()  for line in lines]
    lines = [(start, end, int(cost)) for start, end, cost in lines if start and end and cost]
    return lines



def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    travel_min, _ = t.travelling_salesman(data)

    result = travel_min

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    _, travel_max = t.travelling_salesman(data)

    result = travel_max
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day9s1.txt")
    part_01("day9.txt")

    print()

    part_02("day9s1.txt")
    part_02("day9.txt")

