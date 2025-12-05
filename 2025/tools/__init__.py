import numpy as np

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


