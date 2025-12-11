
def part_01(r: int, c: int) -> None:
    result = code_value(r, c)
    print(f"Part 1: result = {result}")

def part_02() -> None:
    result = 0
    print(f"Part 2: result = {result}")

def grid_value(row: int, column: int) -> int:
    row = row - 1
    column = column - 1
    diagonal = row + column
    diagonal_start = (diagonal * (diagonal + 1)) // 2 + 1
    offset = column
    index = diagonal_start + offset
    return index

def code_value(row: int, column: int) -> int:
    index = grid_value(row, column)
    print("index =", index)
    start_value = 20151125
    multiplier = 252533
    modulus = 33554393

    index = index - 1  
    value = pow(multiplier, index, modulus) * start_value %modulus
    print(value)
    return value


if __name__ == "__main__":
    part_01(3010, 3019)

