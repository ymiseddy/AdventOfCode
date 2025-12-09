import tools as t
import math
import numpy as np
import re
import functools as ft

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    lines = [list(line) for line in lines]
    return lines


def print_grid(data: list) -> None:
    for row in data:
        print("".join(row))
    print()

def reduce_8_directions(callback, grid: list, x: int, y: int, initial):
    xlen = len(grid)
    ylen = len(grid[0])
    result = initial
    p = np.array([x,y])
    for d in t.cardinal_and_diagonal_directions:
        n = p + d
        if n[0] < 0 or n[0] >= xlen or n[1] < 0 or n[1] >= ylen:
            continue
        result = callback(result, grid[n[1]][n[0]])
    return result


def step_grid(data: list) -> list:
    xlen = len(data)
    ylen = len(data[0])
    new_grid = [["." for _ in range(xlen)] for _ in range(ylen)]
    for y in range(ylen):
        for x in range(xlen):
            new_grid[y][x] = data[y][x]
            count = 0
            p = np.array([x,y])
            count = reduce_8_directions(lambda acc, c: acc + (1 if c == "#" else 0), data, x, y, 0)

            c = data[y][x] 
            if c == "#":
                if count < 2 or count > 3:
                    new_grid[y][x] = "."
            if c == ".":
                if count == 3:
                    new_grid[y][x] = "#"
    return new_grid

def part_01(filename: str, count: int) -> None:
    result = 0
    data = load_data(filename)
    xlen = len(data)
    ylen = len(data[0])
    #print("Initial State:")
    #print_grid(data)
    for step in range(count):
        data = step_grid(data)
        #print_grid(data)
    
    dd = np.array(data)
    result = len(dd[dd == "#"])

    print(f"Part 1: result = {result}")

def part_02(filename: str, count) -> None:
    result = 0
    data = load_data(filename)
    xlen = len(data)
    ylen = len(data[0])

    # Corner lights always on
    data[0][0] = 'X'
    data[0][xlen-1] = 'X'
    data[ylen-1][0] = 'X'
    data[ylen-1][xlen-1] = 'X'

    #print("Initial State:")
    #print_grid(data)
    for step in range(count):
        data = step_grid(data)
        #print_grid(data)

    dd = np.array(data)
    result = len(dd[dd != "."])
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day18s1.txt", 4)
    part_01("day18.txt", 100)

    print()

    part_02("day18s1.txt", 5)
    part_02("day18.txt", 100)

