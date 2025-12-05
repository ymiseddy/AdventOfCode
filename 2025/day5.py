import tools as t

def load_data(filename: str) -> list:
    text = t.load(filename)
    lines = text.splitlines()
    data = lines

    ranges = []
    ingredients = []

    last_idx = 0
    for (x, l) in enumerate(lines):
        if l == "":
            last_idx = x
            break
        min, max = l.split("-")
        ranges.append((int(min), int(max)))

    for l in lines[last_idx+1:]:
        ingredients.append(int(l))
    return (ranges, ingredients)


def part_01(filename: str) -> None:
    ranges, ingredients = load_data(filename)
    result = 0
    for ingredient in ingredients:
        for (min, max) in ranges:
            if min <= ingredient and ingredient <= max:
                result += 1
                break

    print(f"Part 1: {result}")

def part_02(filename: str) -> None:
    ranges, ingredients = load_data(filename)
    result = 0

    # Sort ranges by the start value - this helps to catch
    # overlaps
    ranges.sort(key=lambda x: x[0])

    prev_max = 0
    for (min, max) in ranges:

        # Catch overlapping ranges
        if max <= prev_max:
            # This works becaus we sorted the ranges by min value
            continue

        if min <= prev_max:
            min = prev_max + 1

        prev_max = max
        result += (max - min) + 1
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part_01("day5s1.txt")
    part_01("day5.txt")
    print()
    part_02("day5s1.txt")
    part_02("day5.txt")
