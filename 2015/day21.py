import tools as t
import math
import numpy as np
import re
import heapq
from collections.abc import Iterable

boss = np.array((100, 8, 2))  # hit points, damage, armor
player_base = np.array((100, 0, 0))  # hit points, damage, armor

weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
]

armors = [
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
]

rings = [
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
]


def find_winner(player, boss) -> (int, int, int):
    result = 0
    ph, pd, pa = player
    bh, bd, ba = boss

    damage_to_boss = max(1, pd - ba)
    boss_rounds = bh // damage_to_boss
    if bh % damage_to_boss != 0:
        boss_rounds += 1
    damage_to_player = max(1, bd - pa)
    player_rounds = ph // damage_to_player
    if ph % damage_to_player != 0:
        player_rounds += 1

    if player_rounds >= boss_rounds:
        result = 1
    else:
        result = 0
    return result, player_rounds, boss_rounds

def simulate_fight(player, boss) -> int:
    result = 0
    ph, pd, pa = player
    bh, bd, ba = boss

    damage_to_boss = max(1, pd - ba)
    damage_to_player = max(1, bd - pa)
    while True:
        bh -= damage_to_boss
        if bh <= 0:
            result = 1
            break
        ph -= damage_to_player
        if ph <= 0:
            result = 0
            break
    return result

def enumerate_changes(equipment) -> Iterable[(int, int, list[int])]:
    (w, a, r) = equipment
    changes = []

    # change weapon
    for nw in range(len(weapons)):
        if nw != w:
            yield (nw, a, r)

    # change armor
    for na in range(len(armors)):
        if na != a:
            orig_cost = armors[a][1] if a else 0
            yield (w, na, r)

    # remove armor
    if a >= 0:
        yield (w, -1, r)

    # add ring
    if len(r) < 2:
        for nr in range(len(rings)):
            if nr not in r:
                cost = rings[nr][1]
                yield (w, a, r + (nr,))

    # remove ring
    for i in range(len(r)):
        nr = r[:i] + r[i+1:]
        cost = -rings[r[i]][1]
        yield (w, a, nr)

    # change ring
    for i in range(len(r)):
        for nr in range(len(rings)):
            if nr not in r:
                nrings = tuple(r[:i] + (nr,) + r[i+1:])
                yield (w, a, nrings)


def compute_player(equipment) -> (np.array, int):
    (w,a,r) = equipment
    player = player_base.copy()
    weapon = weapons[w]
    armor = armors[a] if a >=0 else ("", 0, 0, 0)
    player_rings = [rings[i] for i in r]
    
    cost = weapon[1] + armor[1] + sum(r[1] for r in player_rings)

    player = player_base.copy()
    player[1:] += np.array(weapon[2:]) + \
    np.array(armor[2:]) + \
    sum(np.array(r[2:]) for r in player_rings)  # damage

    return player, cost

def min_cost_win(base_state) -> int:
    base_state = tuple(base_state)
    result = 0
    heap = []

    visited = set()
    initial_player, initial_cost = compute_player(base_state)
    heapq.heappush(heap, (initial_cost, base_state,))

    min_cost_win = math.inf
    min_cost_state = None
    while heap:
        cost, state = heapq.heappop(heap)
        print(cost,state)
        if state in visited:
            continue
        visited.add(state)
        player, _ = compute_player(state)
        winner, _, _ = find_winner(player, boss)
        if winner == 0:
            if cost < min_cost_win:
                min_cost_win = cost
                min_cost_state = state
                continue
    
        for new_state in enumerate_changes(state):
            if new_state not in visited:
                _, new_cost = compute_player(new_state)  # for debugging
                print(new_cost, new_state)
                heapq.heappush(heap, (new_cost, new_state,))
    print("min cost win:", min_cost_win, min_cost_state)
    return min_cost_win, min_cost_state
    
def max_cost_lose(base_state) -> int:
    base_state = tuple(base_state)
    result = 0
    heap = []

    visited = set()
    initial_player, initial_cost = compute_player(base_state)
    heapq.heappush(heap, (-initial_cost, base_state,))

    max_cost_lose = 0
    max_cost_state = None
    while heap:
        cost, state = heapq.heappop(heap)
        print(-cost,state)
        if state in visited:
            continue
        visited.add(state)
        player, _ = compute_player(state)
        winner, _, _ = find_winner(player, boss)
        if winner == 0:
            if -cost > max_cost_lose:
                max_cost_lose = -cost
                max_cost_state = state
                continue
    
        for new_state in enumerate_changes(state):
            if new_state not in visited:
                _, new_cost = compute_player(new_state)  # for debugging
                print(new_cost, new_state)
                heapq.heappush(heap, (-new_cost, new_state,))
    print("max cost lose:", max_cost_lose, max_cost_state)
    return max_cost_lose, max_cost_state

def part_01() -> None:
    base_state = (w, a, r) = (0, -1, tuple())

    winning_cost, state = min_cost_win(base_state)

    print(f"Part 1: {state} result = {winning_cost}")

def part_02() -> None:
    base_state = (w, a, r) = (4, 4, (4,5,))

    losing_cost, state = max_cost_lose(base_state)

    print(f"Part 2: {state} result = {losing_cost}")


if __name__ == "__main__":
    #part_01()
    print()
    part_02()

