import tools as t
import math
import numpy as np
import re

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

vowel_check = re.compile(r"[aeiou]")
duplicate_letter = re.compile(r"([a-z])\1")
forbidden = re.compile(r"ab|cd|pq|xy")
def is_nice(line: str) -> bool:
    if len(vowel_check.findall(line)) < 3:
        return False
    if not duplicate_letter.search(line):
        return False
    if forbidden.search(line):
        return False
    return True

def part_01(filename: str) -> None:
    result = 0

    data = load_data(filename)
    nice = [is_nice(line) for line in data]
    result = sum([1 for n in nice if n])
    print(f"Part 1: result = {result}")

def is_nice2(line: str) -> bool:
    pair_check = re.compile(r"([a-z]{2}).*\1")
    repeat_check = re.compile(r"([a-z]).\1")
    if not pair_check.search(line):
        return False
    if not repeat_check.search(line):
        return False
    return True

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    nice = [is_nice2(line) for line in data]
    result = sum([1 for n in nice if n])
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day5s1.txt")
    part_01("day5.txt")

    print()

    part_02("day5s2.txt")
    part_02("day5.txt")

