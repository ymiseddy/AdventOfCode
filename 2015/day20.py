import tools as t
import math
import numpy as np
import re
from typing import Generator

def find_factors(n: int) -> Generator[int, None, None]:
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i

def get_presents(n: int) -> int:
    result = 0
    for x in find_factors(n):
        result += 10 * x
    return result

def part_01(n: int) -> None:
    result = 1
    while True:
        p = get_presents(result)
        print(f"House {result} has {p} presents")
        if p >= n:
            break
        result += 1
    print(f"Part 1: {n} - result = {result}")


count = {}
def get_presents_02(n: int) -> int:
    result = 0
    for x in find_factors(n):
        if x not in count:
            count[x] = 0
        if count[x] < 50:
            count[x] += 1
            result += 11 * x
    return result

def part_02(n: int) -> None:
    result = 1
    while True:
        p = get_presents_02(result)
        print(f"House {result} has {p} presents")
        if p >= n:
            break
        result += 1
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    for j in range(1, 11):
        part_01(j)
    #part_01(33100000)

    part_02(33100000)
    print()


