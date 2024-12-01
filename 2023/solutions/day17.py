from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import heapq

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

dirs = {
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(1, 0), (-1, 0)],
    (1, 0): [(0, 1), (0, -1)],
    (-1, 0): [(0, 1), (0, -1)]
}

def djikstra(graph, x, y, in_row, dir, heat_loss, vis, target):
    q = []
    heapq.heappush(q, (heat_loss, x, y, in_row, dir, None, None))
    print(target)
    came_from = {}
    while q:
        heat_loss, x, y, in_row, dir, prevx, prevy = heapq.heappop(q)
        if (x, y) == target:
            print(heat_loss, x, y, in_row, dir)
        if (x, y) == target:
            came_from[(x, y)] = (prevx, prevy)
            return heat_loss, came_from
        if (x, y, in_row, dir) in vis.keys() and heat_loss >= vis[(x, y, in_row, dir)]:
            continue
        came_from[(x, y)] = (prevx, prevy)
        vis[(x, y, in_row, dir)] = heat_loss
        if dir is None:
            poss = [(1, 0), (0, 1)]
        else:
            poss = dirs[dir]
        if in_row < 3 and dir is not None:
            poss.append(dir)
        i = -1
        for dx, dy in poss:
            i += 1
            tx, ty = x + dx, y + dy
            if (ty, tx) not in graph.keys():
                continue
            heapq.heappush(q, (heat_loss + graph[(ty, tx)], tx, ty, 1 if i < 2 else in_row + 1, (dx, dy), x, y))




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
    graph = {}
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            graph[(y, x)] = int(ch)
    vis = {}
    ans, came_from = djikstra(graph, 0, 0, 0, None, 0, vis, (len(data) - 1, len(data[0]) - 1))
    data = [[ch for ch in line] for line in data]
    cur = (len(data[0]) - 1, len(data) - 1)
    data[cur[1]][cur[0]] = "*"
    while cur != (0, 0):
        cur = came_from[cur]
        data[cur[1]][cur[0]] = "*"
        print(cur)
    for line in data:
        print("".join(line))
    #print(came_from)

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
    if False:
        i = 0
        s = ""
        d = {}
        u = set()
        l = []
        ans = 0
        for line in data:
            pass
        for ini in ints:
            pass


def main():
    day = 17
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    #ans1 = solve1([x for x in data])
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
