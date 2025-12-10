import tools as t
import math
import numpy as np
import re
import heapq

boss = np.array((100, 8, 2))  # hit points, damage, armor
player_base = np.array((100, 0, 0))  # hit points, damage, armor

weapons = [
	("Dagger", 8, 4, 0),
	("Shortsword", 10, 5, 0),
	("Warhammer", 25, 6, 0),
	("Longsword", 40, 7, 0),
	("Greataxe", 74, 8, 0),
]

armor = [
        {"None", 0, 0, 0},
	("Leather", 13, 0, 1),
	("Chainmail", 31, 0, 2),
	("Splintmail", 53, 0, 3),
	("Bandedmail", 75, 0, 4),
	("Platemail", 102, 0, 5),
]

rings = [
        ("None", 0, 0, 0),
        ("None", 0, 0, 0),
	("Damage +1", 25, 1, 0),
	("Damage +2", 50, 2, 0),
	("Damage +3", 100, 3, 0),
	("Defense +1", 20, 0, 1),
	("Defense +2", 40, 0, 2),
	("Defense +3", 80, 0, 3),
]

def pick(items, n):
    return np.array([0] + list(items[n][2:]))

def find_winner(player, boss) -> int:
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
    return result

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

def part_01() -> None:
    player = player_base.copy()
    player += pick(weapons, 1)
    player += pick(armor, 1)
    player += pick(rings, 2)
    player += pick(rings, 3)
    result = 0
    print(player)
    print(boss)


    result1 = find_winner(player, boss)
    print("Result should be the same as simulating the fight:")
    result2 = simulate_fight(player, boss)
    print(f"find_winner: {result1}, simulate_fight: {result2}")
    assert result1 == result2

    result = result1


    print(f"Part 1: result = {result}")

def part_02() -> None:
    result = 0
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    part_01()

    print()

    part_02()

