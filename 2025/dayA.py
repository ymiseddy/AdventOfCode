import tools as t
import math
import numpy as np
import re
from scipy.optimize import milp
from scipy.optimize import LinearConstraint
from scipy.optimize import linprog

import heapq

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    data = []
    for line in lines:
        parts = line.split(" ")
        lights = list(parts[0])[1:-1]
        commands = parts[1:]
        pinouts = []
        for cmd in commands:
            cmd_parts = [int(x) for x in cmd[1:-1].split(",")]
            pinouts.append(cmd_parts)
        data.append((lights, pinouts[0:-1], pinouts[-1]))
    return data

def eval_light(lights: list, buttons: list) -> list:
    copy = lights[:]
    for b in buttons:
        copy[b] = "#" if copy[b] == "." else "."
    return copy

def machine_01(machine: list) -> (int, list):
    target, pinouts, _ = machine

    def dijkstra(start: list, target: list) -> (int, list):
        queue = []
        heapq.heappush(queue, (0, 0, start, []))
        visited = set()

        while queue:
            cost, steps, current, btns = heapq.heappop(queue)
            state_tuple = tuple(current)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)

            if current == target:
                return steps, btns

            for pinout in pinouts:
                new_btns = btns + [pinout]
                next_state = eval_light(current, pinout)
                heapq.heappush(queue, (cost + 1, steps + 1, next_state, new_btns))

        return math.inf

    start = ["." for _ in target]
    result = dijkstra(start, target)
    return result


def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for machine in data:
        steps, btns = machine_01(machine)
        #print("".join(machine[0]), steps, btns)
        result += steps

    print(f"Part 1: result = {result}")

def eval_joltage(joltages: list, buttons: list) -> list:
    copy = joltages[:]
    for b in buttons:
        copy[b] += 1
    return copy

def machine_02(machine: list) -> (int, list):
    _, pinouts, target = machine
    lights, buttons, joltages = machine

    # Helper function to convert button presses to a vector of 
    # 1s and 0s representing the effect on joltages
    def btn_to_effect(buttons, sz) -> np.array:
        result = np.zeros(sz)
        for b in buttons:
            result[b] = 1
        return result


    effects = np.array([btn_to_effect(b, len(joltages)) for b in buttons])

    joltages = np.array(joltages)

    # Transpose effects so that each row corresponds to a joltage
    A = effects.T
    B = joltages
    coefficients = np.ones(len(buttons), dtype=np.int64)
    
    res = linprog(coefficients, 
                  A_eq=A, 
                  b_eq=B, 
                  bounds=(0, None), 
                  method="highs", 
                  integrality=True)
    coefs = np.array(res.x, dtype=np.int64)
    
    return round(res.fun), coefs

    # b_u = np.array(joltages)
    # b_l = np.array(joltages)
    # constraints = LinearConstraint(A, b_l, b_u)
    # integrality = np.ones(len(buttons), dtype=np.int64)

    # res = milp(c=coefficients, constraints=constraints, integrality=integrality)

    

    coef = np.array([int(x) for x in res.x])
    result = int(res.fun)

    tt = coef * effects.T
    sum = np.array([int(x) for x in tt.sum(axis=1)])
    match = np.array_equal(sum, joltages)
    if not match:
        print("Mismatch in machine:")
        print("Buttons: ", buttons)
        print("Joltages: ", joltages)
        print("Computed sum: ", sum)
        print("Coefficients: ", coef)
        print("Effects:\n", effects)
        print("Result: ", tt)
        print("Sum: ", sum)
        print("Target: ", joltages)
        print(match)
        #assert match
    
    return result, coef, match

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for machine in data:
        steps, btns = machine_02(machine)
        print("".join(machine[0]), steps, btns)
        result += steps

    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("dayAs1.txt")
    part_01("dayA.txt")

    print()

    part_02("dayAs1.txt")
    part_02("dayA.txt")

