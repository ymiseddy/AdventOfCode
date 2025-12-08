import numpy as np
import itertools as it
import math

def load(name: str):
    with open(name, "r") as f:
        data = f.read()
    return data

def int_columns(data):
    lines = data.splitlines()
    # We want to split each line by spaces and convert to integers.
    columns = []
    for line in lines:
        nums = [int(x) for x in line.split()]
        for i, num in enumerate(nums):
            if len(columns) <= i:
                columns.append([])
            columns[i].append(num)
    # Convert to numpy arrays
    for i in range(len(columns)):
        columns[i] = np.array(columns[i])
    return np.array(columns)


cardinal_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cardinal_and_diagonal_directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def travelling_salesman(paths):
    locations = set()
    costs = {}

    for start, end, cost in paths:
        locations.add(start)
        locations.add(end)
        costs[(start, end)] = int(cost)
        costs[(end, start)] = int(cost)

    min_cost = math.inf
    max_cost = 0

    for perm in it.permutations(locations):
        total_cost = 0
        for i in range(len(perm) - 1):
            total_cost += costs[(perm[i], perm[i + 1])]
        min_cost = min(min_cost, total_cost)
        max_cost = max(max_cost, total_cost)

    return min_cost, max_cost
