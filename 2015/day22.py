import tools as t
import math
import numpy as np
import heapq

boss = np.array((55, 8, 0))  # hit points, damage, mana
player_base = np.array((50, 0, 500))  # hit points, damage, mana

spells = [
    # name, cost, damage, health, armor, mana, duration
    ("Magic Missile", 53, 4, 0, 0, 0, 0),
    ("Drain", 73, 2, 2, 0, 0, 0),
    ("Shield", 113, 0, 0, 7, 0, 6),
    ("Poison", 173, 3, 0, 0, 0, 6),
    ("Recharge", 229, 0, 0, 0, 101, 5),
]

quiet = True
def list_spells():
    for idx, spell in enumerate(spells):
        name, cost, damage, health, armor, mana, duration = spell
        print(f"{idx}: {name}")
        print(f"    Cost: {cost}")
        print(f"    Damage: {damage}")
        print(f"    Health: {health}")
        print(f"    Armor: {armor}")
        print(f"    Mana: {mana}")
        print(f"    Duration: {duration}")


def simulate_fight(player, boss, spell_casts, hard: bool = False) -> tuple(int, int):
    """ Simulate a fight between player and boss given a sequence of spell casts.
    Return result (1=win, -1=loss, 0=incomplete) and remaining mana.
    """
    result = 0
    armor = 0
    ph, pd, pm = player
    bh, bd, _ = boss

    if not quiet:
        print()
        print("=== New Fight Simulation ===")
        print()

    round = 0
    # Effect = (name, timer, armor, damage, mana)
    effects = []

    def print_status():
        if not quiet:
            print("     Boss HP:", bh, "Player HP:", ph, "Mana:", pm, "Armor:", armor)

    def run_effects():
        nonlocal armor, ph, pm, bh
        armor = 0
        new_effects = []
        for name, timer, e_armor, e_damage, e_mana in effects:
            if e_armor > 0:
                armor += e_armor
            if e_damage > 0:
                bh -= e_damage
            if e_mana > 0:
                pm += e_mana
            if timer - 1 > 0:
                new_effects.append([name, timer - 1, e_armor, e_damage, e_mana])
            if not quiet:
                print("    Effect:", name, "Timer:", timer - 1)
        effects[:] = new_effects

    while ph > 0 and pm > 0 and bh > 0:

        if not quiet:
            print("Player turn:")
        if hard:
            if not quiet:
                print("     Hard mode: player loses 1 HP.")
            ph -= 1
            if ph <= 0:
                result = -1
                break
        run_effects()
        print_status()
        # Player's turn
        if round >= len(spell_casts):
            if not quiet:
                print("     No more spells to cast.")
            result = 0 # Incomplete.
            break

        spell_idx = spell_casts[round]
        if not quiet:
            print("     Spell index to cast:", spell_idx)
        spell = spells[spell_idx]
        if not quiet:
            print(f"     Casting {spell}")
        name, cost, damage, health, s_armor, mana, duration = spell
        if pm <= cost:
            # Not enough mana
            result = -1 # Loss
            break
        pm -= cost
        if duration > 0:
            effects.append([name, duration, s_armor, damage, mana])
        else:
            ph += health
            bh -= damage
            if bh <= 0:
                result = 1 # Win
                break

        print_status()

        # Boss's turn
        if not quiet:
            print("Boss turn:")
        run_effects()
        if bh <= 0:
            result = 1 # Win
            break
        damage_taken = max(1, bd - armor)
        if not quiet:
            print("     Boss attacks for", damage_taken, "damage.")
        ph -= damage_taken
        if ph <= 0:
            result = -1 # Loss
            break

        print_status()
        round += 1
    print_status()

    return result, pm

def test_simulation():
    """ Test the fight simulation with known scenarios. """
    # Test simulateion
    btest = np.array((13, 8, 0))  # hit points, damage, mana
    ptest = np.array((10, 0, 250))  # hit points, damage, mana
    spells = (3, 0)
    fight_result, remaining_mana = simulate_fight(ptest, btest, spells)
    print("Test fight result:", fight_result, "Remaining mana:", remaining_mana)
    assert fight_result == 1
    assert remaining_mana == 24


    btest = np.array((14, 8, 0))  # hit points, damage, mana
    fight_result, remaining_mana = simulate_fight(ptest, btest, spells)
    print("Test fight result:", fight_result, "Remaining mana:", remaining_mana)

    assert fight_result == -1
    assert remaining_mana == 24

    fight_result, remaining_mana = simulate_fight(ptest, btest, ())
    print("Test fight result:", fight_result, "Remaining mana:", remaining_mana)

    assert fight_result == 0
    assert remaining_mana == 250

def cost_function(remaining_mana, state, next_state):
    return sum(spells[i][1] for i in next_state)

def next_states(remaining_mana, state):
    for idx, spell in enumerate(spells):
        if idx in state and spell[6] > 0:
            duration = math.ceil(spell[6] / 2)

            # Find the last occurrence of idx in state
            spell_index = len(state) - 1 - state[::-1].index(idx)

            if spell_index + duration > len(state):
                # Spell is already active
                continue
        if spell[1] > remaining_mana:
            continue
        new_state = state + (idx,)
        yield new_state



def dijkstra(initial_state, boss, player, hard: bool = False) -> int:
    result = 0
    heap = []
    heapq.heappush(heap, (0, initial_state))
    visited = set()
    winning_cast = None
    while heap:
        cost, state = heapq.heappop(heap)
        if state in visited:
            continue
        visited.add(state)
        #print("Visited:", state, cost)

        # Process state
        player_state = player.copy()
        boss_state = boss.copy()
        spell_casts = state
        fight_result, remaining_mana = simulate_fight(player_state, boss_state, spell_casts, hard)
        if fight_result == 1:
            # Win
            if not quiet:
                print("Found winning state with cost:", cost, "and spell casts:", spell_casts)
            result = cost
            winning_cast = spell_casts
            break
        elif fight_result == -1:
            # Loss
            continue

        # Generate new states

        new_states = next_states(remaining_mana, state)
        for new_state in new_states:
            new_cost = cost_function(remaining_mana, state, new_state)
            if new_state in visited:
                continue
            print("pushing", remaining_mana, new_state, new_cost)
            heapq.heappush(heap, (new_cost, new_state))

    return result, winning_cast

def part_01(boss, player) -> None:

    def result(state):
        fight_result, remaining_mana = simulate_fight(player, boss, state)
        if fight_result == 1:
            return True, state
        if fight_result == 0:
            return None, remaining_mana
        else:
            return False, remaining_mana

    initial_state = ()
    res, cost = t.dijkstra(initial_state, next_states, cost_function, result)
    casting = [spells[i][0] for i in res]
    total_cost = sum(spells[i][1] for i in res)
    print("Winning spell cast sequence:", casting)
    print("Total mana cost:", total_cost)
    print(f"Part 1 (general): result = {cost}")


def part_02(boss, player) -> None:

    idx_spell_list = [(idx, spell) for idx, spell in enumerate(spells)]

    def visit(state):
        fight_result, remaining_mana = simulate_fight(player, boss, state, hard=True)
        if fight_result == 1:
            return True, state
        if fight_result == 0:
            return None, remaining_mana
        else:
            return False, remaining_mana

    initial_state = ()
    res, cost = t.dijkstra(initial_state, next_states, cost_function, visit)
    casting = [spells[i][0] for i in res]
    total_cost = sum(spells[i][1] for i in res)
    print("Winning spell cast sequence:", casting)
    print("Total mana cost:", total_cost)
    print()
    print(f"Part 2 (general): result = {cost}")



if __name__ == "__main__":
    part_01(boss, player_base)
    print()
    part_02(boss, player_base)
