from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


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
    digged = set()
    x, y = 0, 0
    digged.add((x, y))
    dimap = {
        "R": (1, 0),
        "L": (-1, 0),
        "D": (0, 1),
        "U": (0, -1)
    }
    for line in data:
        a = line.split(" ")
        di = a[0]
        dis = int(a[1])
        for i in range(dis):
            x += dimap[di][0]
            y += dimap[di][1]
            digged.add((x, y))
    maxx = max([x[0] for x in digged])
    minx = min([x[0] for x in digged])
    maxy = max([x[1] for x in digged])
    miny = min([x[1] for x in digged])
    vals = [a for a in dimap.values()]
    #print(digged)
    while True:
        addd = set()
        x = random.randint(minx, maxx)
        y = random.randint(miny, maxy)
        wrong = False
        horizon = [(x, y)]
        addd.add((x, y))
        i = 0
        while i < len(horizon):
            print(i, len(horizon))
            x, y = horizon[i]
            if (x, y) in digged:
                i += 1
                continue
            #addd.add((x, y))
            for dx, dy in vals:
                tx, ty = x + dx, y + dy
                if (tx, ty) in digged:
                    continue
                if tx < minx or tx > maxx or ty < miny or ty > maxy:
                    wrong = True
                    break
                if (tx, ty) in addd:
                    continue
                horizon.append((tx, ty))
                addd.add((tx, ty))
            i += 1
            if wrong:
                break
        if not wrong:
            break
        print("Was wrong")
    for a in addd:
        digged.add(a)
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
    return len(digged)


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    digged = set()
    x, y = 0, 0
    digged.add((x, y))
    dimap = {
        "R": (1, 0),
        "L": (-1, 0),
        "D": (0, 1),
        "U": (0, -1)
    }
    for line in data:
        a = line.split(" ")[2]
        dis = a[2:-2]
        di = a[-2]
        di = "RDLU"[int(di)]
        dis = int(dis, base=16)
        for i in range(dis):
            x += dimap[di][0]
            y += dimap[di][1]
            digged.add((x, y))
        print(line)  # Fuck
    maxx = max([x[0] for x in digged])
    minx = min([x[0] for x in digged])
    maxy = max([x[1] for x in digged])
    miny = min([x[1] for x in digged])
    vals = [a for a in dimap.values()]
    #print(digged)
    while True:
        addd = set()
        x = random.randint(minx, maxx)
        y = random.randint(miny, maxy)
        wrong = False
        horizon = [(x, y)]
        addd.add((x, y))
        i = 0
        while i < len(horizon):
            print(i, len(horizon))
            x, y = horizon[i]
            if (x, y) in digged:
                i += 1
                continue
            #addd.add((x, y))
            for dx, dy in vals:
                tx, ty = x + dx, y + dy
                if (tx, ty) in digged:
                    continue
                if tx < minx or tx > maxx or ty < miny or ty > maxy:
                    wrong = True
                    break
                if (tx, ty) in addd:
                    continue
                horizon.append((tx, ty))
                addd.add((tx, ty))
            i += 1
            if wrong:
                break
        if not wrong:
            break
        print("Was wrong")
    for a in addd:
        digged.add(a)
    return len(digged)


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
