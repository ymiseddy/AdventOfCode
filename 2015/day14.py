import tools as t
import math
import numpy as np
import re

# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

matchRe = re.compile("^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$")


def load_data(filename) -> list:
    data = t.load(filename)
    lines = data.splitlines()
    data = [matchRe.match(line).groups() for line in lines]
    data = [(r, int(s), int(d), int(rs)) for (r, s, d, rs) in data]
    return data

def part_01(filename: str, time: int) -> None:
    result = 0
    data = load_data(filename)
    for (rein, speed, duration, rest) in data:
        cycle_duration = duration + rest
        cycles = time//cycle_duration
        mod = time % cycle_duration

        distance = cycles * duration * speed
        if mod > duration:
            distance += speed * duration
        else:
            distance += speed * mod

        result = max(result, distance)
        print(f"{rein} - {distance}")
    print(f"Part 1: result = {result}")

def part_02(filename: str, time: int) -> None:
    result = 0
    data = load_data(filename)

    standings = {}
    for (rein, speed, duration, rest) in data:
        standings[rein] = [0, 0]

    for t in range(0, time + 1):
        max_distance = 0
        for rein, speed, duration, rest in data:
            distance, points = standings[rein]
            p = t % (duration + rest)
            if p < duration:
                distance += speed
            standings[rein][0] = distance

            if distance > max_distance:
                max_distance = distance
        # standings[winner][1] += 1
        for rein, st in standings.items():
            if st[0] == max_distance:
                st[1] += 1


    for rein, st in standings.items():
        print(f"{rein}: {st[0]} km - {st[1]} points")
        if st[1] > result:
            result = st[1]


    print(f"Part 2: result = {result}")
    print()


if __name__ == "__main__":
    part_01("day14s1.txt", 1000)
    part_01("day14.txt", 2503)

    print()

    part_02("day14s1.txt", 1000)
    part_02("day14.txt", 2503)

