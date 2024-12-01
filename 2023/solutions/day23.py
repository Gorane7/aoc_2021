from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import sys
sys.setrecursionlimit(9999999)

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def dfs(data, cur, visited):
    #print(cur)
    if cur[1] == len(data) - 1:
        return [len(visited)]
    if cur in visited:
        return []
    visited.add(cur)
    x, y = cur
    if data[y][x] in "^>v<":
        if data[y][x] == "^":
            return dfs(data, (x, y - 1), visited)
        if data[y][x] == ">":
            return dfs(data, (x + 1, y), visited)
        if data[y][x] == "<":
            return dfs(data, (x - 1, y), visited)
        return dfs(data, (x, y + 1), visited)
    poss = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or ty < 0 or tx >= len(data[0]) or ty >= len(data) or data[ty][tx] == "#":
            continue
        if (tx, ty) in visited:
            continue
        poss += dfs(data, (tx, ty), {a for a in visited})
    return poss

def dfs2(data, cur, visited, mm, cur_length):
    #print(cur)
    if cur[1] == len(data) - 1:
        return cur_length
    if cur in visited:
        return []
    visited.add(cur)
    x, y = cur
    poss = []

    for neighbour, dis in mm[cur].items():
        #print(neighbour)
        if neighbour in visited:
            continue
        poss += dfs2(data, neighbour, {a for a in visited}, mm, cur_length + dis)
    return poss

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or ty < 0 or tx >= len(data[0]) or ty >= len(data) or data[ty][tx] == "#":
            continue
        if (tx, ty) in visited:
            continue
        poss += dfs2(data, (tx, ty), {a for a in visited})
    return poss


def create_forced_moves(data, cur, visited, allow_split):
    #print(cur, visited)
    x, y = cur
    #if y == len(data) - 1:
    #    return [cur, len(visited)]
    poss = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or ty < 0 or tx >= len(data[0]) or ty >= len(data) or data[ty][tx] == "#":
            continue
        if (tx, ty) in visited:
            continue
        poss.append((tx, ty))
    ans = []
    if allow_split:
        for a in poss:
            ans.append(create_forced_moves(data, a, {cur}, False))
        return ans
    print(cur, poss)
    if len(poss) > 1:
        return cur, len(visited)
    if poss:
        visited.add(cur)
        return create_forced_moves(data, poss[0], visited, False)


def shorten(data, cur, mm):
    a = create_forced_moves(data, cur, set(), True)
    #print(cur, a)
    mm[cur] = {}
    for b in a:
        if b:
            dest, dist = b
            mm[cur][dest] = dist
    for b in a:
        if b:
            dest, dist = b
            if dest not in mm.keys():
                shorten(data, dest, mm)


def solve1(data):

    ints     = [extract_ints(x) for x in data]
    # first  = map_lines(data[:1], [int], ",")
    parsed   = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed   = my_map(parsed, lambda x: x)
    data     = my_map(data, lambda x: x)
    #data    = my_map(data, lambda x: [int(a) for a in x.split(" ")])
    print()
    print("!!!SAMPLE INPUT!!!")
    [print(x) for x in data[:20]]
    print("!!!END SAMPLE INPUT!!!")
    print()


    # SOLUTION
    i = 0
    s = ""
    d = {}
    u = set()
    l = []
    ans = 0
    cur = (1, 0)
    visited = set()
    distances = dfs(data, cur, visited)
    print(distances)
    for line in data:
        pass
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
    return max(distances)


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    cur = (1, 0)
    visited = set()
    #distances = dfs2(data, cur, visited)
    mm = {}
    shorten(data, cur, mm)
    #print()
    #print(mm)
    for key, value in mm.items():
        print(key, value)
    distances = dfs2(data, cur, visited, mm, 0)
    print(distances)
    return max(distances)


def main():
    day = 23
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    #ans1 = solve1([x for x in data])
    #ans2 = solve2([x for x in data])
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")

    testdata = parse_input(-1)
    if testdata:
        ans1t = solve1([x for x in testdata])
        ans2t = solve2([x for x in testdata])
        print(f"Answer a: {ans1}")
        print(f"Answer b: {ans2}")
        print(f"Test a: {ans1t}")
        print(f"Test b: {ans2t}")


if __name__ == '__main__':
    main()
