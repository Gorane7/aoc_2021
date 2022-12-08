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
    grid = []
    vis = []
    for line in data:
        row = []
        visr = []
        for number in line:
            row.append(int(number))
            visr.append(0)
        grid.append(row)
        vis.append(visr)
    for i in range(len(grid)):
        high = -1
        for j in range(len(grid[i])):
            if grid[i][j] > high:
                ans += 1
                vis[i][j] = 1
                high = grid[i][j]
        high = -1
        for j in range(len(grid[i]) - 1, -1, -1):
            if grid[i][j] > high:
                ans += 1
                high = grid[i][j]
                vis[i][j] = 1
    for j in range(len(grid[0])):
        high = -1
        for i in range(len(grid)):
            if grid[i][j] > high:
                ans += 1
                high = grid[i][j]
                vis[i][j] = 1
        high = -1
        for i in range(len(grid) - 1, -1, -1):
            if grid[i][j] > high:
                ans += 1
                high = grid[i][j]
                vis[i][j] = 1

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return sum([sum(x) for x in vis])


def find_score(y, x, grid):
    val = grid[y][x]
    score = 1
    this = 0
    for i in range(y - 1, -1, -1):
        if grid[i][x] < val:
            this += 1
        else:
            this += 1
            break
    score *= this
    this = 0
    for i in range(y + 1, len(grid)):
        if grid[i][x] < val:
            this += 1
        else:
            this += 1
            break
    score *= this
    this = 0
    for i in range(x - 1, -1, -1):
        if grid[y][i] < val:
            this += 1
        else:
            this += 1
            break
    score *= this
    this = 0
    for i in range(x + 1, len(grid[0])):
        if grid[y][i] < val:
            this += 1
        else:
            this += 1
            break
    score *= this
    return score



def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    grid = []
    for line in data:
        row = []
        for number in line:
            row.append(int(number))
        grid.append(row)
    best = 0
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            best = max(best, find_score(y, x, grid))
    return best


def main():
    day = 8
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
