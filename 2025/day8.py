import tools as t
import math
import numpy as np
import re
import itertools as it

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    lines = [line.split(",") for line in lines]
    lines = [[np.int64(num) for num in line] for line in lines]
    lines = [tuple(line) for line in lines]
    return lines

def part_01(filename: str, maxcon: int) -> None:
    result = 0
    data = load_data(filename)
    distances = []
    count = 0
    for combo in it.combinations(data, 2):
        count +=1
        d = np.linalg.norm(np.array(combo[0]) - np.array(combo[1]))
        distances.append((d, combo))

    # sort distances
    distances.sort(key=lambda x: x[0])

    pointCircuit = {}
    circuitPoints = {}
    for idx, d in enumerate(data):
        pointCircuit[d] = idx
        circuitPoints[idx] = set()
        circuitPoints[idx].add(d)

    for (distance, combo) in distances[0:maxcon]:
        c0 = pointCircuit.get(combo[0], None)
        c1 = pointCircuit.get(combo[1], None)

        if c0 is not None and c1 is not None:
            # Need to merge circuits
            # Move points from c1 to c0
            if c0 == c1:
                continue
            for point in circuitPoints[c1]:
                pointCircuit[point] = c0
                circuitPoints[c0].add(point)
            del circuitPoints[c1]
            continue
        else:
            raise "This should not happen"

    # Sort the circuits by size
    sortedCircuits = sorted(circuitPoints.items(), key=lambda x: len(x[1]), reverse=True)
    for circuit in sortedCircuits:
        print(f"Circuit {circuit[0]}: size {len(circuit[1])}")

    result = math.prod([len(circuit[1]) for circuit in sortedCircuits[0:3]])
    print(f"Part 1: result = {result}")

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    distances = []
    count = 0
    for combo in it.combinations(data, 2):
        count +=1
        d = np.linalg.norm(np.array(combo[0]) - np.array(combo[1]))
        distances.append((d, combo))

    # sort distances
    distances.sort(key=lambda x: x[0])

    pointCircuit = {}
    circuitPoints = {}
    for idx, d in enumerate(data):
        pointCircuit[d] = idx
        circuitPoints[idx] = set()
        circuitPoints[idx].add(d)

    for (distance, combo) in distances:
        c0 = pointCircuit.get(combo[0], None)
        c1 = pointCircuit.get(combo[1], None)

        if c1 not in circuitPoints:
            raise ValueError("This should not happen")
        if c0 not in circuitPoints:
            raise ValueError("This should not happen")

        if c0 is not None and c1 is not None:
            # Need to merge circuits
            # Move points from c1 to c0
            if c0 == c1:
                continue
            for point in circuitPoints[c1]:
                pointCircuit[point] = c0
                circuitPoints[c0].add(point)
            del circuitPoints[c1]
            if (len(circuitPoints) == 1):
                print("All points connected")
                result = combo[0][0]*combo[1][0]
                print(f"Boxes: {combo[0]}, {combo[1]}")
                break
        else:
            raise "This should not happen"

    print(f"Part 2: result = {result}")



if __name__ == "__main__":
    #part_01("day8s1.txt", 10)
    part_01("day8.txt", 1000)

    print()

    #part_02("day8s1.txt")
    part_02("day8.txt")

