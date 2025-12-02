import tools as t

def load_data(filename):
    text = t.load(filename)
    lines = text.splitlines()
    data = lines
    return data


def part_01(filename="day1s1.txt"):
    result = 0
    data = load_data(filename)

    print(f"Part 1: {result}")


def part_02(filename="day1s1.txt"):
    result = 0
    data = load_data(filename)

    print(f"Part 2: {result}")

if __name__ == "__main__":
    part_01("day2.txt")
    print()
    part_02("day2.txt")

