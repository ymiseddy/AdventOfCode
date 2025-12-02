import tools as t

def load_data(filename):
    data = t.load(filename)
    rangeStrs = data.split(",")
    ranges = []
    for r in rangeStrs:
        (start, end) = r.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def part_01(filename="day1s1.txt"):
    result = 0
    ranges = load_data(filename)
    for (start, end) in ranges:
        for n in range(start, end + 1):
            x = str(n)
            splitPoint = len(x) // 2
            firstHalf = x[:splitPoint]
            secondHalf = x[splitPoint:]
            if firstHalf == secondHalf:
                result += n

    print(f"Part 1: {result}")


def part_02(filename="2025/day1s1.txt"):
    result = 0
    ranges = load_data(filename)
    for (start, end) in ranges:
        for n in range(start, end + 1):
            x = str(n)
            ln = len(x)
            for i in range(1, (ln//2) + 1):
                s = x[:i]
                ls = len(s)
                if (ln % ls) == 0:
                    if s * (ln // len(s)) == x:
                        result += n
                        break
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part_01("day2.txt")
    print()
    part_02("day2.txt")
