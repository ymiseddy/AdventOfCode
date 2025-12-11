import numpy as np
import numpy.typing as npt
import heapq

def load(name: str):
    with open(name, "r") as f:
        data = f.read()
    return data

def ints(data: str) -> list[int]:
    lines = data.splitlines()
    result = [int(x) for x in lines]
    return result

cardinal_directions = [np.array(direction) for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
cardinal_and_diagonal_directions = [np.array(direction) for direction in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]]

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


def dijkstra(initial_state, next_states, cost_function, result):
    """ Generalized Dijkstra's algorithm implementation.

        Parameters:
            initial_state: starting state
            next_states: function(visit_result, state) -> generator of next states
            cost_function: function(visit_result, state, next_state) -> cost
            result: function(state) -> (success: bool | None, visit_result)
       
       Returns:
            (result_state, total_cost) if goal state reached, else None

        For the result function:
            success = True: goal state reached, return visit_result
            success = False: invalid state / dead end, stop processing
            success = None: continue processing


    """

    heap = []
    heapq.heappush(heap, (0, initial_state))
    visited = set()
    while heap:
        cost, state = heapq.heappop(heap)
        if state in visited:
            continue
        visited.add(state)

        # Process state
        success, res = result(state)

        if success == False:
            continue

        if success:
            return res, cost

        # Generate new states
        for next_state in next_states(res, state):
            new_cost = cost_function(res, state, next_state)
            if next_state not in visited:
                heapq.heappush(heap, (new_cost, next_state))

    return None, None
