from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import sys

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def set_to_grid(seti):
    maxx = float("-inf")
    minx = float("inf")
    maxy = float("-inf")
    miny = float("inf")
    for x, y in seti:
        maxx = max(maxx, x)
        minx = min(minx, x)
        maxy = max(maxy, y)
        miny = min(miny, y)
    grid = [["." for x in range(maxx - minx + 1)] for y in range(maxy - miny + 1)]
    for x, y in seti:
        grid[y - miny][x - minx] = "#"
    return grid


def solve1(data):

    ints = [extract_ints(x) for x in data]
    # first = map_lines(data[:1], [int], ",")
    parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed = my_map(parsed, lambda x: x)

    # SOLUTION
    i = 0
    s = ""
    d = {}
    u = set()
    l = []
    ans = 0
    elves = set()
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "#":
                elves.add((x, y))
    dirs = [[(0, -1), (1, -1), (-1, -1)], [(0, 1), (1, 1), (-1, 1)], [(-1, 0), (-1, 1), (-1, -1)], [(1, 0), (1, -1), (1, 1)]]
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i in range(10):
        propositions = {}
        for x, y in elves:
            all_empty = True
            for dx, dy in deltas:
                if (x + dx, y + dy) in elves:
                    all_empty = False
                    break
            if all_empty:
                propositions[(x, y)] = [(x, y)]
                continue
            proposed = False
            for checks in dirs:
                all_empty = True
                for dx, dy in checks:
                    if (x + dx, y + dy) in elves:
                        all_empty = False
                        break
                if all_empty:
                    dest = (x + checks[0][0], y + checks[0][1])
                    if dest not in propositions.keys():
                        propositions[dest] = []
                    propositions[dest].append((x, y))
                    proposed = True
                    break
            if not proposed:
                propositions[(x, y)] = [(x, y)]
        new_elves = set()
        for key, value in propositions.items():
            if len(value) == 1:
                new_elves.add(key)
                continue
            for val in value:
                new_elves.add(val)
        elves = new_elves
        dirs.append(dirs.pop(0))
    for line in set_to_grid(elves):
        for ch in line:
            if ch == ".":
                ans += 1

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return ans


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    ans = 0
    elves = set()
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "#":
                elves.add((x, y))
    dirs = [[(0, -1), (1, -1), (-1, -1)], [(0, 1), (1, 1), (-1, 1)], [(-1, 0), (-1, 1), (-1, -1)], [(1, 0), (1, -1), (1, 1)]]
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    moved = True
    while moved:
        ans += 1
        moved = False
        propositions = {}
        for x, y in elves:
            all_empty = True
            for dx, dy in deltas:
                if (x + dx, y + dy) in elves:
                    all_empty = False
                    break
            if all_empty:
                propositions[(x, y)] = [(x, y)]
                continue
            proposed = False
            for checks in dirs:
                all_empty = True
                for dx, dy in checks:
                    if (x + dx, y + dy) in elves:
                        all_empty = False
                        break
                if all_empty:
                    dest = (x + checks[0][0], y + checks[0][1])
                    if dest not in propositions.keys():
                        propositions[dest] = []
                    propositions[dest].append((x, y))
                    proposed = True
                    break
            if not proposed:
                propositions[(x, y)] = [(x, y)]
        new_elves = set()
        for key, value in propositions.items():
            if len(value) == 1:
                if value[0] != key:
                    moved = True
                new_elves.add(key)
                continue
            for val in value:
                new_elves.add(val)
        elves = new_elves
        dirs.append(dirs.pop(0))
    return ans


def main():
    day = 23
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    ans1 = solve1([x for x in data])
    ans2 = solve2([x for x in data])
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
