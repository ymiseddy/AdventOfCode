import tools as t
import math
import numpy as np
import re

forbidden_letters = {'i', 'o', 'l'}

def password_policy(password: str) -> bool:
    good = True
    # Requires at least 3 straight increasing letters
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(password[i + 2]):
            break
    else:
        return False
    
    # Cannot contain i, o, or l
    for c in forbidden_letters:
        if c in password:
            return False

    # Must contain at least two different, non-overlapping pairs of letters
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2
        else:
            i += 1
    if len(pairs) < 2:
        return False

    return good

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

def next_password(input_password: str) -> str:
    password = input_password
    while True:
        # increment password
        password = list(password)
        i = len(password) - 1
        while i >= 0:
            if password[i] == 'z':
                password[i] = 'a'
                i -= 1
            else:
                password[i] = chr(ord(password[i]) + 1)
                break
        password = "".join(password)
        if password_policy(password):
            result = password
            return result


def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for line in data:
        # increment password until it meets policy
        password = line
        result = next_password(password)

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    result = next_password(data[0])
    print(f"After first increment: {result}")
    result = next_password(result)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    #part_01("day11s1.txt")
    part_01("day11.txt")

    #print()

    #part_02("day11s1.txt")
    part_02("day11.txt")

