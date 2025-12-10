import tools as t
import math
import numpy as np
import re
import z3

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


def eval_joltage(joltages: list, buttons: list) -> list:
    copy = joltages[:]
    for b in buttons:
        copy[b] += 1
    return copy

def machine_02(machine: list) -> (int, list):
    _, buttons, target = machine

    # Helper function to convert button presses to a vector of 
    # 1s and 0s representing the effect on joltages
    def btn_to_effect(buttons, sz) -> np.array:
        result = np.zeros(sz)
        for b in buttons:
            result[b] = 1
        return result

    solver = z3.Optimize()

    button_presses = [z3.Int(f"b_{i}") for i,b in enumerate(buttons)]
    for b in button_presses:
        solver.add(b >= 0)

    target_joltages = [z3.Int(f"t_{i}") for i in range(len(target))]
    for i, target_joltage in enumerate(target_joltages):
        solver.add(target_joltage == target[i])
        W = [button_presses[bi] for bi,button in enumerate(buttons) if i in button]
        target_joltage == z3.Sum(W)
        constraint = target_joltage == z3.Sum(W)
        solver.add(constraint)

    solver.minimize(z3.Sum(button_presses))
    result = 0
    coef = []
    match = False

    if solver.check() == z3.sat:
        model = solver.model()
        coef = [model[b].as_long() for b in button_presses]
        result = sum(coef)
    else:
        print("UNSAT")

    return result, coef

def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    for machine in data:
        steps, btns = machine_02(machine)
        #print("".join(machine[0]), steps, btns)
        result += steps

    print(f"Part 2: result = {result}")


if __name__ == "__main__":

    print()

    part_02("dayAs1.txt")
    part_02("dayA.txt")

