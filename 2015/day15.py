import tools as t
import math
import numpy as np
import re

#Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8

matchRe = re.compile(r'^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$')

def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    lines = [matchRe.match(line).groups() for line in lines]
    lines = [(i, np.int64(c), np.int64(d), np.int64(f), np.int64(t), np.int64(ca)) for (i, c, d, f, t, ca) in lines]
    return lines


def dp(tp, seg, n, scorer):
    if len(seg) == n - 1:
        tt = sum(seg)
        m = tp - tt
        seg = seg + [m]
        res = scorer(seg)
        # print(seg, res)
        return res, seg

    result = 0
    quants = None
    mx = 100 - sum(seg)
    for x in range(mx + 1):
        sub, quant = dp(tp, seg + [x], n, scorer)
        if sub > result:
            result = sub
            quants = quant

    return result, quants

def part1_score(ing):
    values = np.array([i[1:-1] for i in ing])
    def score(arr):
        tt = np.array([values[x] * c for x, c in enumerate(arr)] )
        y = np.sum(tt, axis=0)
        y[y < 0] = 0
        total = np.prod(y)
        return np.prod(y)
    return score



def part_01(filename: str) -> None:
    result = 0
    data = load_data(filename)
    ing = len(data)
    sp = 100
    scorer = part1_score(data)
    result = dp(sp,[], ing, scorer)


    print(f"Part 1: result = {result}")


def part2_score(ing):
    values = np.array([i[1:-1] for i in ing])
    calories = np.array([i[-1]  for i in ing])
    def score(arr):
        tt_calories = np.sum(calories * arr)
        if tt_calories != 500:
            return 0
        tt = np.array([values[x] * c for x, c in enumerate(arr)] )
        y = np.sum(tt, axis=0)
        y[y < 0] = 0
        total = np.prod(y)
        return np.prod(y)
    return score


def part_02(filename: str) -> None:
    result = 0
    data = load_data(filename)
    ing = len(data)
    sp = 100
    scorer = part2_score(data)
    result = dp(sp,[], ing, scorer)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01("day15s1.txt")
    part_01("day15.txt")

    print()

    part_02("day15s1.txt")
    part_02("day15.txt")

