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
    for line in data:
        pass
    for ini in ints:
        hist = []
        new_vals = []
        vals = ini
        hist.append(vals)
        while True:
            new_vals = []
            print(len(vals))
            for i in range(len(vals) - 1):
                new_vals.append(vals[i + 1] - vals[i])
            vals = new_vals
            hist.append(vals)
            bb = True
            for qwe in vals:
                if qwe:
                    bb = False
            if bb:
                break
        exp = 0
        for vall in hist[::-1]:
            exp = exp + vall[-1]
        ans += exp

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
    for line in data:
        pass
    for ini in ints:
        hist = []
        new_vals = []
        vals = ini
        hist.append(vals)
        while True:
            new_vals = []
            print(len(vals))
            for i in range(len(vals) - 1):
                new_vals.append(vals[i + 1] - vals[i])
            vals = new_vals
            hist.append(vals)
            bb = True
            for qwe in vals:
                if qwe:
                    bb = False
            if bb:
                break
        exp = 0
        for vall in hist[::-1]:
            exp = vall[0] - exp
        ans += exp
    return ans


def main():
    day = 9
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
