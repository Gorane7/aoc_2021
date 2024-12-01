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
    ans = 0
    seq = data[0]
    qwe = {}
    for line in data[2:]:
        asd = line.split(" = ")
        key = asd[0]
        a, b = asd[1][1:-1].split(", ")
        qwe[key] = (a, b)
    cur = "AAA"
    while True:
        a = seq[ans % len(seq)]
        if a == "L":
            cur = qwe[cur][0]
        else:
            cur = qwe[cur][1]
        ans += 1
        if cur == "ZZZ":
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
    seq = data[0]
    qwe = {}
    for line in data[2:]:
        asd = line.split(" = ")
        key = asd[0]
        a, b = asd[1][1:-1].split(", ")
        qwe[key] = (a, b)
    locations = []
    for key in qwe.keys():
        if key[-1] == "A":
            locations.append(key)
    vals = [0 for i in range(6)]
    while True:
        new_locations = []
        a = seq[ans % len(seq)]
        for cur in locations:
            if a == "L":
                new_locations.append(qwe[cur][0])
            else:
                new_locations.append(qwe[cur][1])
        ans += 1
        locations = new_locations
        for i, loc in enumerate(locations):
            if loc[-1] == "Z" and vals[i] == 0:
                vals[i] = ans
        if 0 not in vals:
            break
    lcm = 1
    for a in vals:
        lcm = math.lcm(a, lcm)
    return lcm


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
