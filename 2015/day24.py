import tools as t
import math
from collections.abc import Generator
from itertools import combinations

def load_data(filename: str) -> list[int]:
    data = t.load(filename)
    lines = data.splitlines()
    values = [int(line) for line in lines]
    return values

def using_dijkstra():
    def visit(state: tuple[int]) -> tuple[bool | None, tuple[int]]:
        weight = sum(state)
        print(f"Visiting state: {state}, {weight}")
        if weight == target:
            return True, state

        if weight < target:
            return None, state

        return False, state

    def cost_function(_result: tuple[int, ...], _state: tuple[int, ...], next_state: tuple[int,...]) -> tuple[int, int]:
        return len(next_state), math.prod(next_state)

    def next_states(_result: tuple[int], state: tuple[int]) -> Generator[tuple[int, ...]]:
        for item in data:
            if item in state:
                continue
            new_state = state + (item,)
            yield new_state

    initial_group = ()
    res, cost = t.dijkstra(initial_group, next_states, cost_function, visit)
    print(f"Found group: {res} with cost: {cost}")
    result = cost[1]

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    data.sort(reverse=True)
    total_weight = sum(data)
    if total_weight % 3 != 0:
        raise ValueError("Total weight not divisible by 3")

    target = total_weight // 3

    for i in range(1, len(data)):
        min_prod = math.inf
        found = None
        for combo in combinations(data, i):
            if sum(combo) == target:
                prod = math.prod(combo)
                if prod < min_prod:
                    min_prod = prod
                    found = combo
        if found is not None:
            result = min_prod
            break
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    data.sort(reverse=True)
    total_weight = sum(data)
    if total_weight % 3 != 0:
        raise ValueError("Total weight not divisible by 3")

    target = total_weight // 4

    for i in range(1, len(data)):
        min_prod = math.inf
        found = None
        for combo in combinations(data, i):
            if sum(combo) == target:
                prod = math.prod(combo)
                if prod < min_prod:
                    min_prod = prod
                    found = combo
        if found is not None:
            result = min_prod
            break
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    # 29728298883 - too high

    part_01("day24s1.txt")
    part_01("day24.txt")

    print()

    part_02("day24s1.txt")
    part_02("day24.txt")

