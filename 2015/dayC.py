import tools as t
import math
import numpy as np
import re
import json

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

def walk(struct: list | dict) -> int:
    result = 0
    if isinstance(struct, dict):
        for i in struct.values():
            if isinstance(i, int):
                result += i
            elif isinstance(i, list) or isinstance(i,dict):
                result +=walk(i)
    elif isinstance(struct, list):
        for i in struct:
            if isinstance(i, int):
                result += i
            elif isinstance(i, list) or isinstance(i,dict):
                result +=walk(i)
    return result

def walk2(struct: list | dict) -> int:
    result = 0
    if isinstance(struct, dict):
        for i in struct.values():
            if isinstance(i, str) and i == "red":
                return 0

        for i in struct.values():
            if isinstance(i, int):
                result += i
            elif isinstance(i, list) or isinstance(i,dict):
                result +=walk2(i)
    elif isinstance(struct, list):
        for i in struct:
            if isinstance(i, int):
                result += i
            elif isinstance(i, list) or isinstance(i,dict):
                result +=walk2(i)
    return result


def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for line in data:
        struct = json.loads(line)
        result = walk(struct)

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for line in data:
        struct = json.loads(line)
        result = walk2(struct)
    print(f"Part 2: result = {result}")

# 9092 - low

if __name__ == "__main__":
    part_01("dayCs1.txt")
    part_01("dayC.txt")

    print()

    part_02("dayCs2.txt")
    part_02("dayC.txt")

