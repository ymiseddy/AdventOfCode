import tools as t
import math
import numpy as np
import re

def pair(x):
    for z in range(len(x)-1):
        yield x[z], x[z+1]

def check_digits(x: int) -> tuple[bool, bool, int]:
    s = str(x)
    has_double = False
    for idx in range(len(s) - 1):
        a = s[idx]
        b = s[idx + 1]
        if a == b:
            has_double = True
        elif a > b:
            return False, False, idx
   
    return True, has_double, 0

def check_digits2(x: int) -> tuple[bool, bool, int]:
    s = str(x)
    has_double = False

    prev_a = ''
    for idx in range(len(s) - 1):
        a = s[idx]
        b = s[idx + 1]
        if a == b and not has_double and a != prev_a:
            has_double = True
            if idx < len(s) - 2 and s[idx+2] == a:
                has_double = False
        elif a > b:
            return False, False, idx
        prev_a = a
   
    return True, has_double, 0



def part_01() -> None:
    result = 0
    start = 145852
    end = 616942
    x = start
    for x in range(start, end+1):
        is_not_decreasing, has_double, idx = check_digits(x)
        if is_not_decreasing and has_double:
            result += 1
    # 145852-616942 
    print(f"Part 1: result = {result}")

def part_02() -> None:
    result = 0
    start = 145852
    end = 616942
    x = start
    for x in range(start, end+1):
        is_not_decreasing, has_double, idx = check_digits2(x)
        if is_not_decreasing and has_double:
            result += 1
    # 145852-616942 
    print(f"Part 2: result = {result}")
    

if __name__ == "__main__":

    part_01()

    print()

    part_02()

