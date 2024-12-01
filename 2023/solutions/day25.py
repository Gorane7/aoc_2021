from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import sys
sys.setrecursionlimit(10000)

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def find_path(a, b, g, so_far, c):
    if a == b:
        return so_far
    if c > 100:
        return False
    n = random.choice(g[a])
    if n in so_far:
        return find_path(a, b, g, so_far, c + 1)
    so_far.add(n)
    return find_path(n, b, g, so_far, 0)


def find_path_actual(a, b, g, so_far, r):
    if a == b:
        return True
    so_far.add(a)
    for n in g[a]:
        if n in r:
            continue
        if n in so_far:
            continue
        ans = find_path_actual(n, b, g, so_far, r)
        if ans:
            return True
    return False


def test_path(g, r, k):
    for i in range(100):
        ans = find_path_actual(random.choice(k), random.choice(k), g, set(), r)
        if not ans:
            return False
    return True


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
    g = {}
    al = set()
    for line in data:
        a, b = line.split(": ")
        b = b.split(" ")
        al.add(a)
        if a not in g.keys():
            g[a] = []
        for k in b:
            al.add(k)
            if k not in g.keys():
                g[k] = []
            g[a].append(k)
            g[k].append(a)
    al = [x for x in al]
    chosen = {key: 0 for key in al}
    for i in range(10000):
        if i % 100 == 0:
            print(i)
        path = find_path(random.choice(al), random.choice(al), g, set(), 0)
        if path:
            for a in path:
                chosen[a] += 1
    items = chosen.items()
    items = sorted(items, key=lambda x: -x[1])
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            for k in range(j + 1, len(items)):
                r = [items[i][0], items[j][0], items[k][0]]
                test_path(g, r, al)
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
    day = 25
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
