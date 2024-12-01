from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def solve1(data):

    #ints     = [extract_ints(x) for x in data]
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
    graph = {}
    anim = None
    for y, line in enumerate(data):
        for x, sym in enumerate(line):
            if sym == ".":
                graph[(x, y)] = []
            if sym == "S":
                anim = (x, y)
            if sym == "|":
                graph[(x, y)] = [(x, y - 1), (x, y + 1)]
            if sym == "-":
                graph[(x, y)] = [(x - 1, y), (x + 1, y)]
            if sym == "F":
                graph[(x, y)] = [(x + 1, y), (x, y + 1)]
            if sym == "7":
                graph[(x, y)] = [(x - 1, y), (x, y + 1)]
            if sym == "L":
                graph[(x, y)] = [(x + 1, y), (x, y - 1)]
            if sym == "J":
                graph[(x, y)] = [(x - 1, y), (x, y - 1)]
    cons = []
    x, y = anim
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if (x + dx, y + dy) in graph.keys() and anim in graph[(x + dx, y + dy)]:
            cons.append((x + dx, y + dy))
    graph[anim] = cons
    print(anim, cons)
    i = 1
    l, r = graph[anim]
    pl, pr = anim, anim
    vis = {anim, l, r}
    while True:
        cl = [x for x in graph[l] if x not in vis]
        if not cl:
            break
        l = cl[0]
        vis.add(l)
        cr = [x for x in graph[r] if x not in vis]
        if not cr:
            break
        r = cr[0]
        vis.add(r)
        i += 1
    print(len(vis))
    i += 1



    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return i


def solve2u(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    graph = {}
    uns = set()
    anim = None
    for y, line in enumerate(data):
        for x, sym in enumerate(line):
            uns.add((x, y))
            if sym == ".":
                graph[(x, y)] = []
            if sym == "S":
                anim = (x, y)
            if sym == "|":
                graph[(x, y)] = [(x, y - 1), (x, y + 1)]
            if sym == "-":
                graph[(x, y)] = [(x - 1, y), (x + 1, y)]
            if sym == "F":
                graph[(x, y)] = [(x + 1, y), (x, y + 1)]
            if sym == "7":
                graph[(x, y)] = [(x - 1, y), (x, y + 1)]
            if sym == "L":
                graph[(x, y)] = [(x + 1, y), (x, y - 1)]
            if sym == "J":
                graph[(x, y)] = [(x - 1, y), (x, y - 1)]
    cons = []
    x, y = anim
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if (x + dx, y + dy) in graph.keys() and anim in graph[(x + dx, y + dy)]:
            cons.append((x + dx, y + dy))
    graph[anim] = cons
    print(anim, cons)
    i = 1
    l, r = graph[anim]
    pl, pr = anim, anim
    path = []
    vis = set()
    while True:
        cl = [x for x in graph[l] if x not in vis]
        if not cl:
            break
        l = cl[0]
        path.append(l)
        vis.add(l)
        i += 1
    lside = set()
    rside = set()
    lm = {
        (0, 1): (1, 0),
        (0, -1): (-1, 0),
        (1, 0): (-1, 0),
        (-1, 0): (1, 0)
    }
    rm = {
        (0, 1): (-1, 0),
        (0, -1): (1, 0),
        (1, 0): (1, 0),
        (-1, 0): (-1, 0)
    }
    for i in range(-1, len(path) - 1):
        x, y = path[i]
        dx, dy = path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1]
        lx, ly = x + lm[(dx, dy)][0], y + lm[(dx, dy)][1]
        rx, ry = x + rm[(dx, dy)][0], y + rm[(dx, dy)][1]
        if (lx, ly) not in vis:
            lside.add((lx, ly))
        if (rx, ry) not in vis:
            rside.add((rx, ry))
    #print(path)
    print(lside.intersection(rside))
    for a in vis:
        uns.remove(a)
    for a in lside:
        uns.remove(a)
    for a in rside:
        uns.remove(a)
    print(len(uns), len(vis), len(lside), len(rside))
    i += 1
    return i


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    graph = {}
    uns = set()
    anim = None
    for y, line in enumerate(data):
        for x, sym in enumerate(line):
            uns.add((x, y))
            if sym == ".":
                graph[(x, y)] = []
            if sym == "S":
                anim = (x, y)
            if sym == "|":
                graph[(x, y)] = [(x, y - 1), (x, y + 1)]
            if sym == "-":
                graph[(x, y)] = [(x - 1, y), (x + 1, y)]
            if sym == "F":
                graph[(x, y)] = [(x + 1, y), (x, y + 1)]
            if sym == "7":
                graph[(x, y)] = [(x - 1, y), (x, y + 1)]
            if sym == "L":
                graph[(x, y)] = [(x + 1, y), (x, y - 1)]
            if sym == "J":
                graph[(x, y)] = [(x - 1, y), (x, y - 1)]
    cons = []
    x, y = anim
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if (x + dx, y + dy) in graph.keys() and anim in graph[(x + dx, y + dy)]:
            cons.append((x + dx, y + dy))
    graph[anim] = cons
    print(anim, cons)
    i = 1
    l, r = graph[anim]
    pl, pr = anim, anim
    path = []
    vis = set()
    while True:
        cl = [x for x in graph[l] if x not in vis]
        if not cl:
            break
        l = cl[0]
        path.append(l)
        vis.add(l)
        i += 1
    lside = set()
    rside = set()
    lm = {
        (0, 1): (1, 0),
        (0, -1): (-1, 0),
        (1, 0): (-1, 0),
        (-1, 0): (1, 0)
    }
    rm = {
        (0, 1): (-1, 0),
        (0, -1): (1, 0),
        (1, 0): (1, 0),
        (-1, 0): (-1, 0)
    }
    outside = set()
    for i in range(len(data)):
        if (0, i) not in vis:
            outside.add((0, i))
        if (len(data[0]) - 1, i) not in vis:
            outside.add((len(data[0]) - 1, i))
    for i in range(len(data[0])):
        if (i, 0) not in vis:
            outside.add((i, 0))
        if (i, len(data) - 1) not in vis:
            outside.add((i, len(data) - 1))
    added = 1
    print(len(outside))
    new = {x for x in outside}
    while added:
        cout = {x for x in outside}
        newnew = set()
        added = 0
        for x, y in new:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x + dx, y + dy) in graph.keys() and (x + dx, y + dy) not in vis and (x + dx, y + dy) not in outside:
                    outside.add((x + dx, y + dy))
                    newnew.add((x + dx, y + dy))
                    added += 1
        
        new = newnew
        #print(len(new))
    print(len(outside))
    i += 1
    return len(data) * len(data[0]) - len(vis) - len(outside)


def main():
    day = 10
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
