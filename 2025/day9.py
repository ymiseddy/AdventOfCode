import tools as t
import math
import numpy as np
import re
import itertools as it

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    lines = [line.split(",") for line in lines]
    lines = np.array([(np.int32(x), np.int32(y)) for x, y in lines])
    return lines

def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    sides = np.abs([x - y for x,y in it.combinations(data,2)]) + 1
    areas = np.prod(sides, axis=1)
    result = np.max(areas)

    print(f"Part 1: result = {result}")

def trace_poly_edges(data) -> dict:
    edges = {}
    
    minx = np.min(data[:,0])
    maxx = np.max(data[:,0])
    miny = np.min(data[:,1])
    maxy = np.max(data[:,1])

    for y in range(miny, maxy+1):
        edges[y] = [maxx + 2, minx - 2]

    # Create a loop by appending the first point to the end
    p1 = data[0]
    loop = np.append(data[1:], [p1], axis=0)

    # Trace the lines
    for p2 in loop: 
        p = p1.copy()
        sign = np.sign(p2 - p1)
        if edges[p[1]][0] > p[0]:
            edges[p[1]][0] = p[0]
        if edges[p[1]][1] < p[0]:
            edges[p[1]][1] = p[0]

        if edges[p2[1]][0] > p2[0]:
            edges[p2[1]][0] = p2[0]
        if edges[p2[1]][1] < p2[0]:
            edges[p2[1]][1] = p2[0]

        while not np.array_equal(p, p2):
            p += sign
            yy = p[1]
            xx = p[0]
            if xx < edges[yy][0]:
                edges[yy][0] = xx
            if xx > edges[yy][1]:
                edges[yy][1] = xx
        p1 = p2
    return edges

def inside_edges(p1: np.array, p2: np.array, edges: dict) -> bool:
    points = np.array([[p1[0], p1[1]],
              [p1[0], p2[1]],
              [p2[0], p2[1]],
              [p2[0], p1[1]]]);

    # Checking the corners first really speeds things up.
    for p in points:
        yy = p[1]
        xx = p[0]
        if xx < edges[yy][0] or xx > edges[yy][1]:
            return False

    miny = min(p1[1], p2[1])
    maxy = max(p1[1], p2[1])
    minx = min(p1[0], p2[0])
    maxx = min(p1[0], p2[0])

    for y in range(miny, maxy+1):
        if edges[y][0] > minx or edges[y][1] < maxx:
            return False
    return True


def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)

    edges = trace_poly_edges(data)

    found = []
    for x,y in it.combinations(data,2):
        area = np.prod(np.abs(x - y) + 1, axis=0)
        found.append((area, (x,y)))

    found = sorted(found, key=lambda item: item[0], reverse=True)
    found_len = len(found)
    for x, (area, (p1, p2)) in enumerate(found):
        if inside_edges(p1, p2, edges):
            print("Found valid area:", area, "points:", p1, p2)
            result = area
            break

    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day9s1.txt")
    part_01("day9.txt")

    print()

    part_02("day9s1.txt")
    part_02("day9.txt")

