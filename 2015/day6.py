import tools as t
import math
import numpy as np
import re

commandParse = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    outputs = []
    for line in lines:
        match = commandParse.match(line)
        assert match is not None
        command = match.group(1)
        x1 = int(match.group(2))
        y1 = int(match.group(3))
        x2 = int(match.group(4))
        y2 = int(match.group(5))
        outputs.append((command, x1, y1, x2, y2))
    return outputs

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    grid = np.zeros((1000, 1000), dtype=bool)
    for command, x1, y1, x2, y2 in data:
        if command == "turn on":
            grid[x1:x2+1, y1:y2+1] = True
        elif command == "turn off":
            grid[x1:x2+1, y1:y2+1] = False
        elif command == "toggle":
            grid[x1:x2+1, y1:y2+1] = ~grid[x1:x2+1, y1:y2+1]

    result = np.sum(grid)
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    grid = np.zeros((1000, 1000), dtype=int)
    for command, x1, y1, x2, y2 in data:
        if command == "turn on":
            grid[x1:x2+1, y1:y2+1] += 1
        elif command == "turn off":
            grid[x1:x2+1, y1:y2+1] -= 1
            grid[grid < 0] = 0
        elif command == "toggle":
            grid[x1:x2+1, y1:y2+1] += 2
    result = np.sum(grid)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day6s1.txt")
    part_01("day6.txt")

    print()

    part_02("day6s1.txt")
    part_02("day6.txt")

