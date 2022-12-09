from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

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
    visited = set()
    dird = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }
    visited.add((0, 0))
    stack = [[0, 0] for _ in range(2)]
    for line in data:
        spl = line.split(" ")
        dir = spl[0]
        am = int(spl[1])
        d = dird[dir]
        for i in range(am):
            stack[0][0] += d[0]
            stack[0][1] += d[1]
            for j in range(1):
                dx = stack[j + 1][0] - stack[j][0]
                dy = stack[j + 1][1] - stack[j][1]
                if abs(dx) >= 2 or abs(dy) >= 2:
                    if dx > 0:
                        stack[j + 1][0] -= 1
                    if dx < 0:
                        stack[j + 1][0] += 1
                    if dy > 0:
                        stack[j + 1][1] -= 1
                    if dy < 0:
                        stack[j + 1][1] += 1
            visited.add((stack[-1][0], stack[-1][1]))
    for ini in ints:
        pass

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')

    my_shelf.close()
    return len(visited)


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    visited = set()
    dird = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }
    visited.add((0, 0))
    stack = [[0, 0] for _ in range(10)]
    for line in data:
        spl = line.split(" ")
        dir = spl[0]
        am = int(spl[1])
        d = dird[dir]
        for i in range(am):
            stack[0][0] += d[0]
            stack[0][1] += d[1]
            for j in range(9):
                dx = stack[j + 1][0] - stack[j][0]
                dy = stack[j + 1][1] - stack[j][1]
                if abs(dx) >= 2 or abs(dy) >= 2:
                    if dx > 0:
                        stack[j + 1][0] -= 1
                    if dx < 0:
                        stack[j + 1][0] += 1
                    if dy > 0:
                        stack[j + 1][1] -= 1
                    if dy < 0:
                        stack[j + 1][1] += 1
            visited.add((stack[-1][0], stack[-1][1]))
    return len(visited)


def main():
    day = 9
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
