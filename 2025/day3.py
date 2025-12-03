import tools as t

def load_data(filename):
    text = t.load(filename)
    lines = text.splitlines()
    data = lines
    return data


def part_01(filename="day3s1.txt"):
    result = 0
    data = load_data(filename)
    for bank in data:
        max = 0
        for idx, c1 in enumerate(bank):
            for c2 in bank[idx + 1:]:
                val = int(c1 + c2)
                if val > max:
                    max = val
        result += max

    print(f"Part 1: {result}")

def part_02(filename="day1s1.txt"):
    result = 0
    data = load_data(filename)
    for bank in data:
        val = []
        lidx = 0
        for b in range(12):
            max = 0
            maxidx = 0
            ct = len(bank) - (12 - b) + 1
            for idx, c in enumerate(bank[lidx:ct]):
                if int(c) > max:
                    max = int(c)
                    maxidx = idx + lidx + 1
            val.append(str(max))
            lidx = maxidx
        joined = ''.join(val)
        result += int(joined)


    print(f"Part 2: {result}")

if __name__ == "__main__":
    part_01("day3s1.txt")
    part_01("day3.txt")
    print()
    part_02("day3s1.txt")
    part_02("day3.txt")

