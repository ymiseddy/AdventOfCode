import tools as t
import math
import numpy as np
import re

def load_data(filename: str) -> np.ndarray[np.int64]:
    data = t.load(filename)
    return t.ints(data)

def part_01(filename: str) -> None:
    data = np.array(load_data(filename))
    result = np.sum((data // 3) - 2)
    print(f"Part 1: result = {result}")
 
def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for i in data:
        fuel = i
        while True:
            fuel = (fuel // 3) - 2
            if fuel <= 0:
                break
            result += fuel

    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day01.txt")

    print()

    part_02("day01.txt")

