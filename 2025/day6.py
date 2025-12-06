import tools as t
import math
import re

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()

    # Split lines by spaces
    for i in range(len(lines)):
        lines[i] = lines[i].split()

    # Transpose the lines to get columns
    lines = list(map(list, zip(*lines)))

    return lines

def load_data_2(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    return lines

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for row in data:
        op = row[-1]
        numbers = [int(x) for x in row[:-1]]
        result += math.prod(numbers) if op == "*" else sum(numbers)
    print(f"Part 1: result = {result}")


def part_02(filename: str) -> None:
    result = 0
    data = load_data_2(filename)

    findOpRe = re.compile(r"[\*\+]\s+")
    ops = data[-1].split()

    # We need to find the widths of each column
    ops_col = findOpRe.findall(data[-1])
    widths = [len(x) for x in ops_col]
    problems = []
    for w in widths:
        problems.append([])

    # Split each line into the problems
    for line in data[:-1]:
        s = 0
        for i, w in enumerate(widths):
            problems[i].append(line[s:(s+w)])
            s += w

    for i, problem in enumerate(problems):
        numbers = []
        digit_length = len(problem[0])
        for x in range(digit_length):
            digits = [p[x] for p in problem if p[x] != ' ']
            if len(digits) == 0:
                continue
            number = int("".join(digits))
            numbers.append(number)
        result += math.prod(numbers) if ops[i] == "*" else sum(numbers)

    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day6s1.txt")
    part_01("day6.txt")

    print()

    part_02("day6s1.txt")
    part_02("day6.txt")

