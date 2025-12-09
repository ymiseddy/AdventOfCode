import tools as t
import math
import numpy as np
import re
from functools import lru_cache
import random
from collections import deque
import heapq

def load_data(filename) -> list:
    data = t.load(filename)
    replacements, source = data.split("\n\n")
    lines = replacements.splitlines()
    lines = [line.split(" => ") for line in lines]
    return (lines, source.strip())

def part_01(filename: str) -> None:
    result = 0
    replacements, source = load_data(filename)

    found = set()
    for old, new in replacements:
        idx = 0
        old_len = len(old)
        while idx != -1:
            idx = source.find(old, idx)
            if idx == -1:
                break
            replaced = source[:idx] + new + source[idx + old_len:]
            found.add(replaced)
            idx += old_len

    result = len(found)

    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    replacements, target = load_data(filename)
    data = load_data(filename)
    initial = "e"
    len_target = len(target)

    def dijkstra(target: str, source: str) -> int:
        # dijkstra's algorithm using the number of characters different 
        # from the target as the cost
        heap = []
        heapq.heappush(heap, (0, 0, target))
        visited = set()

        while heap:
            cost, steps, current = heapq.heappop(heap)
            if current == source:
                return steps
            if current in visited:
                continue
            visited.add(current)

            for new, old in replacements:
                old_len = len(old)
                idx = 0
                while idx != -1:
                    idx = current.find(old, idx)
                    if idx == -1:
                        break
                    replaced = current[:idx] + new + current[idx + old_len:]
                    if replaced not in visited:
                        # calculate cost as number of different characters from source
                        diff = sum(1 for a, b in zip(replaced, source) if a != b) + abs(len(replaced) - len(source))
                        heapq.heappush(heap, (diff, steps + 1, replaced))
                    idx += old_len
        return math.inf


    result = dijkstra(target, initial)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day19s1.txt")
    part_01("day19.txt")

    print()

    part_02("day19s2.txt")
    part_02("day19.txt")

