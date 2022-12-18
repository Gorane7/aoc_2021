from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
from queue import PriorityQueue

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


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
    cubes = set()
    for line in data:
        pass
    for ini in ints:
        cubes.add((ini[0], ini[1], ini[2]))
    for x, y, z in cubes:
        for dx, dy, dz in [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]:
            if (x + dx, y + dy, z + dz) not in cubes:
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

    ints = [extract_ints(x) for x in data]
    # first = map_lines(data[:1], [int], ",")
    parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed = my_map(parsed, lambda x: x)

    # SOLUTION HERE
    ans = 0
    cubes = set()
    inside = set()
    free = set()
    for line in data:
        pass
    xl, yl, zl = [999, 0], [999, 0], [999, 0]
    for ini in ints:
        xl[0] = min(xl[0], ini[0])
        xl[1] = max(xl[1], ini[0])
        yl[0] = min(yl[0], ini[1])
        yl[1] = max(yl[1], ini[1])
        zl[0] = min(zl[0], ini[2])
        zl[1] = max(zl[1], ini[2])
        cubes.add((ini[0], ini[1], ini[2]))
    # print(xl, yl, zl)
    for x, y, z in cubes:
        for dx, dy, dz in [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]:
            new = (x + dx, y + dy, z + dz)
            if new in cubes:
                continue
            if new in inside and new not in cubes:
                continue
            if new in free and new not in cubes:
                ans += 1
                continue
            find(new, inside, free, cubes)
            if new in inside and new not in cubes:
                continue
            if new in free and new not in cubes:
                ans += 1
                continue
            print("ERROR")
    return ans


def find(new, inside, free, cubes):
    is_inside = False
    is_free = False
    queue = PriorityQueue()
    passed = set()
    passed.add(new)
    queue.put((0, new))
    s = 1
    visited = set()
    while not queue.empty():
        dist, loc = queue.get()
        s -= 1
        if loc in visited:
            continue
        if loc in cubes:
            continue
        if loc in inside:
            is_inside = True
            break
        if loc in free:
            is_free = True
            break
        if loc[0] < 0 or loc[0] > 21 or loc[1] < 0 or loc[1] > 20 or loc[2] < 0 or loc[2] > 21:
            is_free = True
            break
        visited.add(loc)
        # print(s)
        x, y, z = loc
        for dx, dy, dz in [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]:
            new = (x + dx, y + dy, z + dz)
            queue.put((dist + 1, new))
            passed.add(new)
            s += 1
    if is_inside:
        while not queue.empty():
            dist, loc = queue.get()
            inside.add(loc)
        for loc in passed:
            inside.add(loc)
        return
    if is_free:
        while not queue.empty():
            dist, loc = queue.get()
            free.add(loc)
        for loc in passed:
            free.add(loc)
        return
    for loc in passed:
        inside.add(loc)


def main():
    day = 18
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
