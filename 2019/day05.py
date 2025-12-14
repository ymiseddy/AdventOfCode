import tools as t
from intcode import IntCode

def part_01(filename: str) -> None:
    result = 0
    comp = IntCode(debug=True)
    comp.load(filename)
    comp.run()
    result = comp.last_output
    print(f"Part 1: result = {result}")

if __name__ == "__main__":
    part_01("day05.txt")

