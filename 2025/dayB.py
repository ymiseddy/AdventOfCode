import tools as t
import math
import numpy as np
import re
from functools import cache

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    out_paths = {}
    for line in lines:
        source, dests = line.split(": ")
        dests_list = dests.split(" ")
        out_paths[source] = dests_list

    return out_paths

def find_paths_02(out_paths, start, end):
    @cache
    def search(current):
        if current == end:
            return 1
        total_paths = sum(search(neighbor) for neighbor in out_paths.get(current, []))
        return total_paths

    return search(start)

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    result = find_paths_02(data, "you", "out")
    print(f"Part 1: result = {result}")


def part_02(filename: str) -> None:

    result = 0
    data = load_data(filename)
  
    svr_fft = find_paths_02(data, "svr", "fft")
    fft_dac = find_paths_02(data, "fft", "dac")
    dac_out = find_paths_02(data, "dac", "out")

    result = svr_fft * fft_dac * dac_out

    print(f"Part 2: result = {result}")

if __name__ == "__main__":
    part_01("dayBs1.txt")
    part_01("dayB.txt")

    print()

    part_02("dayBs2.txt")
    part_02("dayB.txt")
