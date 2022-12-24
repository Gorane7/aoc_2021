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
    for y, line in enumerate(data):
        if line == "":
            break
        for x, ch in enumerate(line):
            if ch != " ":
                grid[(x + 1, y + 1)] = ch
    instructions = data[-1]

    x = 51
    # x = 9
    y = 1
    face = 0
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cache = ""
    for ch in instructions + "F":
        if ch in "LRF":
            dir = ch
            amount = int(cache)
            cache = ""
            dx, dy = d[face]
            for i in range(amount):
                new = (x + dx, y + dy)
                if new not in grid.keys():
                    if face == 0:
                        new = (min([a[0] for a in grid if a[1] == new[1]]), new[1])
                    elif face == 1:
                        new = (new[0], min([a[1] for a in grid if a[0] == new[0]]))
                    elif face == 2:
                        new = (max([a[0] for a in grid if a[1] == new[1]]), new[1])
                    else:
                        new = (new[0], max([a[1] for a in grid if a[0] == new[0]]))
                if grid[new] == "#":
                    break
                x, y = new
            if ch == "L":
                face = (face - 1) % 4
            elif ch == "R":
                face = (face + 1) % 4
            continue
        cache += ch
    print(x, y, face)

    # END SOLUTION
    return 1000 * y + 4 * x + face


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    grid = {}
    for y, line in enumerate(data):
        if line == "":
            break
        for x, ch in enumerate(line):
            if ch != " ":
                grid[(x + 1, y + 1)] = ch
    instructions = data[-1]

    side_length = 50
    x = side_length + 1
    # x = 9
    y = 1
    face = 0
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cache = ""
    for ch in instructions + "F":
        if ch in "LRF":
            dir = ch
            amount = int(cache)
            cache = ""
            dx, dy = d[face]
            for i in range(amount):
                new = (x + dx, y + dy)
                if new not in grid.keys():
                    #   .##
                    #   .#.
                    #   ##.
                    #   #..
                    if face == 0:
                        if y <= side_length:
                            pass
                        elif y <= side_length * 2:
                            pass
                        elif y <= side_length * 3:
                            pass
                        else:
                            pass
                        new = (min([a[0] for a in grid if a[1] == new[1]]), new[1])
                    elif face == 1:
                        new = (new[0], min([a[1] for a in grid if a[0] == new[0]]))
                    elif face == 2:
                        new = (max([a[0] for a in grid if a[1] == new[1]]), new[1])
                    else:
                        new = (new[0], max([a[1] for a in grid if a[0] == new[0]]))
                if grid[new] == "#":
                    break
                x, y = new
            if ch == "L":
                face = (face - 1) % 4
            elif ch == "R":
                face = (face + 1) % 4
            continue
        cache += ch
    print(x, y, face)

    # END SOLUTION
    return 1000 * y + 4 * x + face


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
