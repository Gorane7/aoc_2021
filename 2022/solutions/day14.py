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
    rocks = {}
    min_y = 0
    for line in data:
        steps = line.split(" -> ")
        x, y = None, None
        for step in steps:
            ax, ay = [int(x) for x in step.split(",")]
            min_y = max(min_y, ay)
            if x is None:
                x, y = ax, ay
                continue
            if x != ax:
                for dx in range(min(x, ax), max(x, ax) + 1):
                    rocks[(dx, ay)] = "r"
            else:
                for dy in range(min(y, ay), max(y, ay) + 1):
                    rocks[(ax, dy)] = "r"
            x, y = ax, ay
    falling = False
    while not falling:
        sx, sy = 500, 0
        while True:
            if sy > min_y:
                falling = True
                break
            if (sx, sy + 1) not in rocks.keys():
                sy += 1
                continue
            if (sx - 1, sy + 1) not in rocks.keys():
                sx -= 1
                sy += 1
                continue
            if (sx + 1, sy + 1) not in rocks.keys():
                sy += 1
                sx += 1
                continue
            rocks[(sx, sy)] = "s"
            ans += 1
            break
    for ini in ints:
        pass

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
    rocks = {}
    min_y = 0
    for line in data:
        steps = line.split(" -> ")
        x, y = None, None
        for step in steps:
            ax, ay = [int(x) for x in step.split(",")]
            min_y = max(min_y, ay)
            if x is None:
                x, y = ax, ay
                continue
            if x != ax:
                for dx in range(min(x, ax), max(x, ax) + 1):
                    rocks[(dx, ay)] = "r"
            else:
                for dy in range(min(y, ay), max(y, ay) + 1):
                    rocks[(ax, dy)] = "r"
            x, y = ax, ay
    falling = False
    for x in range(-2000, 2000):
        rocks[(x, min_y + 2)] = "r"
    while not falling:
        sx, sy = 500, 0
        while True:
            if (sx, sy + 1) not in rocks.keys():
                sy += 1
                continue
            if (sx - 1, sy + 1) not in rocks.keys():
                sx -= 1
                sy += 1
                continue
            if (sx + 1, sy + 1) not in rocks.keys():
                sy += 1
                sx += 1
                continue
            rocks[(sx, sy)] = "s"
            ans += 1
            break
        if sx == 500 and sy == 0:
            break
    return ans


def main():
    day = 14
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
