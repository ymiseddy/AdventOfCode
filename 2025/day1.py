import tools as t

def load_data(filename):
    data = t.load(filename)
    lines = data.splitlines()

    r2 = [(x[0] == 'R') * int(x[1:]) + ((x[0] == 'L') * (-int(x[1:]))) for x in lines]
    return r2


def part_01(filename="2025/day1s1.txt"):
    steps = load_data(filename)
    p = 50
    zcount = sum(1 for count in steps if (p := (p + count) % 100) == 0)
    print(f"Part 1: zero count = {zcount}")


def part_02(filename="2025/day1s1.txt"):
    steps = load_data(filename)
    p = 50
    zcount = 0
    for count in steps:
        ztimes = (p - 1) // 100 - (p + count - 1) // 100
        zcount += ztimes 
        p = (p + count) % 100



    print(f"Part 2: zero count = {zcount}")

if __name__ == "__main__":
    part_01("day1s1.txt")
    part_01("day1.txt")

    print()

    part_02("day1s1.txt")
    part_02("day1.txt")
