import tools as t
import math
import numpy as np
import re
from itertools import product
from shapely.geometry import LineString, Point
from collections.abc import  Generator

type Coordinate = tuple[int, int]
type Edge = tuple[Coordinate, Coordinate]
type EdgeList = list[Edge]
type Direction = tuple[str, int]
type DirectionList = list[Direction]


def load_data(filename: str) -> DirectionList:
    data = t.load(filename)
    probs = data.split("\n\n")
    pairs: list[DirectionList] = []
    for prob in probs:
        paths = prob.splitlines()
        path_directions = []
        for path in paths:
            moves = path.split(",")
            directions: DirectionList = [(q[0], int(q[1:])) for q in moves]
            path_directions.append(directions)

        pairs.append(path_directions)
    return pairs 

edges_to_path: dict[Edge, EdgeList] = {}
def path_to_edges(path: DirectionList) -> EdgeList:
    global edges_to_path
    x:int = 0;
    y:int = 0;
    edges: list[tuple[tuple[int,int],tuple[int,int]]] = []
    for dir, quant in path:
        nx: int = x
        ny: int = y

        if dir == "U":
            ny -= quant
        if dir == "D":
            ny += quant
        if dir == "L":
            nx -= quant
        if dir == "R":
            nx += quant
        edge = ((x,y),(nx,ny))
        edges_to_path[edge] = edges
        edges.append(edge)
        x = nx
        y = ny

    return edges

def intersects(a: Edge, b: Edge) -> tuple[int, int] | None:
    line1 = LineString(a)
    line2 = LineString(b)
    int_pt = line1.intersection(line2)
    if isinstance(int_pt, Point):
        pt = (int_pt.x, int_pt.y)
        return pt
    return None

def find_intersections(path_a: DirectionList, path_b: DirectionList) -> Generator[tuple[tuple[int, int], Edge, Edge]]:
    edges_a = path_to_edges(path_a)
    edges_b = path_to_edges(path_b)

    for a,b in product(edges_a, edges_b):
        if (i := intersects(a, b)) is not None:
            intersect = (i,a,b)
            yield intersect

def part_01(filename: str) -> None:
    global edges_to_path
    result = 0
    data = load_data(filename)
    for a,b in data:
        edges_to_path = {}
        result = [x for x, _, _ in find_intersections(a,b) if x != (0.0, 0.0)]
        result = min([(np.linalg.norm(b, ord=1), b) for b in result])
        print(result)

    # 135 too low
    print(f"Part 1: result = {result}")

def walk_path_to_edge(path: EdgeList, edge: Edge, intersection: tuple[int,int]) -> int:
    dist = 0
    for e in path:
        if e == edge:
            dist += np.linalg.norm(np.array(intersection) - np.array(e[0]), ord=1)
            break
        dist += np.linalg.norm(np.array(e[1]) - np.array(e[0]), ord=1)
    return dist

def part_02(filename: str) -> None:
    global edges_to_path
    result = 0,
    data = load_data(filename)
    for a,b in data:
        edges_to_path = {}
        min_dist = math.inf
        intersections = [x for x in find_intersections(a,b) if x[0] != (0.0, 0.0)]
        for intersection, a, b in intersections:
            path_a = edges_to_path[a]
            path_b = edges_to_path[b]
            walk_dist_a = walk_path_to_edge(path_a, a, intersection)
            walk_dist_b = walk_path_to_edge(path_b, b, intersection)
            if (walk_dist_a + walk_dist_b) < min_dist:
                min_dist = walk_dist_a + walk_dist_b
        result = min_dist
        print(result)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    edges_to_path = {}
    #part_01("day03s1.txt")
    edges_to_path = {}
    #part_01("day03.txt")

    print()

    edges_to_path = {}
    part_02("day03s1.txt")
    edges_to_path = {}
    part_02("day03.txt")

