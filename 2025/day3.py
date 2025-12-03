import tools as t

def load_data(filename):
    text = t.load(filename)
    lines = text.splitlines()
    data = lines
    return data



def joltage(data, count):
    result = 0
    for bank in data:
        idx = 0
        val = []
        for b in range(count):
            dist = len(bank) - (count - b) + 1
            idx, v = max(enumerate(bank[:dist]), key=lambda x: int(x[1]))
            val.append(v)
            bank = bank[idx + 1:]
        joined = ''.join(val)
        result += int(joined)
    return result

def part_01(filename="day3s1.txt"):
    data = load_data(filename)
    result = joltage(data, count=2)

    print(f"Part 1: {result}")

def part_02(filename="day1s1.txt"):
    data = load_data(filename)
    result = joltage(data, count=12)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part_01("day3s1.txt")
    part_01("day3.txt")
    print()
    part_02("day3s1.txt")
    part_02("day3.txt")

