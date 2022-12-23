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
    grid = {}
    maxx = 150
    maxy = 200
    # maxx = 17
    # maxy = 12
    for y, line in enumerate(data[:201]):
        for x, ch in enumerate(line):
            grid[(y + 1, x + 1)] = ch
        x += 1
        while x < maxx:
            grid[(y + 1, x + 1)] = " "
            x += 1
    instructions = data[-1]

    x = 51
    y = 1
    face = 0
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cache = ""
    for ch in instructions:
        if ch in "LR":
            dir = ch
            amount = int(cache)
            cache = ""
            dx, dy = d[face]
            for i in range(amount):
                new = (y + dy, x + dx)
                if new not in grid.keys():
                    if new[0] == 0:
                        new = (maxy, new[1])
                    elif new[1] == 0:
                        new = (new[0], maxx)
                    elif new[0] > maxy:
                        new = (1, new[1])
                    elif new[1] > maxx:
                        new = (new[0], 1)
                    else:
                        print("ERROR")
                while grid[new] == " ":
                    new = (new[0] + dy, new[1] + dx)
                    if new not in grid.keys():
                        if new[0] == 0:
                            new = (maxy, new[1])
                        elif new[1] == 0:
                            new = (new[0], maxx)
                        elif new[0] > maxy:
                            new = (1, new[1])
                        elif new[1] > maxx:
                            new = (new[0], 1)
                        else:
                            print("ERROR")
                if grid[new] == "#":
                    break
                y, x = new
            if ch == "L":
                face = (face - 1) % 4
            elif ch == "R":
                face = (face + 1) % 4
            else:
                print("ERROR")
            print(x, y, face)
            continue
        cache += ch
    print(x, y, face)

    # END SOLUTION
    return ans


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE


def main():
    day = 22
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
