import tools as t

cardinal_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cardinal_and_diagonal_directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def load_data(filename):
    text = t.load(filename)
    lines = text.splitlines()
    data = lines
    return data

def count_surrounding(data, x, y) -> int:
    count = 0
    for dx, dy in cardinal_and_diagonal_directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(data) and 0 <= nx < len(data[ny]):
            if data[ny][nx] == '@':
                count += 1
    return count


def compute_removable(data) -> (int, list):
    result = 0
    outmap = []
    for y in range(len(data)):
        outmap.append([])
        for x in range(len(data[y])):
            outmap[y].append(data[y][x])
            if data[y][x] != '@':
                continue
            open = count_surrounding(data, x, y)
            if open < 4:
                outmap[y][x] = 'x'
                result += 1

    newmap = []
    for x in outmap:
        newmap.append("".join(x))

    return result, outmap


def part_01(filename="day3s1.txt"):
    data = load_data(filename)
    result, _ = compute_removable(data)
    print(f"Part 1: {result}")

def part_02(filename="day1s1.txt"):
    data = load_data(filename)
    result = 0
    while True:
        removed, data = compute_removable(data)
        if removed == 0:
            break
        result += removed
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part_01("day4s1.txt")
    part_01("day4.txt")
    print()
    part_02("day4s1.txt")
    part_02("day4.txt")


