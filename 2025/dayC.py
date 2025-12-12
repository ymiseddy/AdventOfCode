from turtle import width
import tools as t
import math
import numpy as np
import itertools as it
import re




def load_data(filename: str):
    data = t.load(filename)
    trees = []

    parts = data.split("\n\n")

    present_sizes = {}
    present_shapes = parts[:-1]
    for idx, present in enumerate(present_shapes):
        size = present.count("#")
        present_sizes[idx] = size

    tree_parts = parts[-1].splitlines()
    for tree_part in tree_parts:
        size, counts_parts = tree_part.split(":")
        width, height = map(int, size.split("x"))
        counts = tuple(map(int, counts_parts.strip().split(" ")))
        trees.append(((width, height), counts))

    return present_sizes, trees

def part_01(filename: str) -> None:
    result = 0
    present_sizes, trees = load_data(filename)

    for (width, height), counts in trees:
        area = width * height
        print(f"Tree {width}x{height} area {area}")
        pack_size = 0
        for idx, count in enumerate(counts):
            present_size = present_sizes[idx]
            pack_size += present_sizes[idx] * count
            print(f"  Present {idx} size {present_size} count {count} pack size {pack_size}")
        
        print(f"Tree {width}x{height} with counts {counts} requires pack size {pack_size}")
        if pack_size <= area:
            result += 1

    print(f"Part 1: result = {result}")



if __name__ == "__main__":
    part_01("dayC.txt")


