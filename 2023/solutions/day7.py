from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
from functools import cmp_to_key

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

def to_num(ch):
    # print(ch)
    return "23456789TJQKA".index(ch)

def to_num2(ch):
    # print(ch)
    return "J23456789TQKA".index(ch)

def compare(x, y):
    x, y = x[0], y[0]
    ax = {}
    ay = {}
    for ch in x:
        if ch not in ax.keys():
            ax[ch] = 0
        ax[ch] += 1
    for ch in y:
        if ch not in ay.keys():
            ay[ch] = 0
        ay[ch] += 1
    vala = 0
    valb = 0
    if 5 in ax.values():
        vala = 5
    elif 4 in ax.values():
        vala = 4
    elif 3 in ax.values() and 2 in ax.values():
        vala = 3
    elif 3 in ax.values():
        vala = 2
    elif len([q for q in ax.values() if q == 2]) > 1:
        vala = 1
    elif 2 in ax.values():
        vala = 0
    else:
        vala = -1

    if 5 in ay.values():
        valb = 5
    elif 4 in ay.values():
        valb = 4
    elif 3 in ay.values() and 2 in ay.values():
        valb = 3
    elif 3 in ay.values():
        valb = 2
    elif len([q for q in ay.values() if q == 2]) > 1:
        valb = 1
    elif 2 in ay.values():
        valb = 0
    else:
        valb = -1
    if vala > valb:
        return 1
    if valb > vala:
        return -1
    for ca, cb in zip(x, y):
        na = to_num(ca)
        nb = to_num(cb)
        if na > nb:
            return 1
        if nb > na:
            return -1
    return 0


def best_val(hand):
    # print(hand)
    tval = -5
    ay = {}
    if "J" in hand:
        for opt in "23456789AKQT":
            tval = max(tval, best_val(hand[:hand.index("J")] + opt + hand[hand.index("J") + 1:]))
        return tval
    for ch in hand:
        if ch not in ay.keys():
            ay[ch] = 0
        ay[ch] += 1
    if 5 in ay.values():
        tval = 5
    elif 4 in ay.values():
        tval = 4
    elif 3 in ay.values() and 2 in ay.values():
        tval = 3
    elif 3 in ay.values():
        tval = 2
    elif len([q for q in ay.values() if q == 2]) > 1:
        tval = 1
    elif 2 in ay.values():
        tval = 0
    else:
        tval = -1
    return tval


def compare2(x, y):
    x, y = x[0], y[0]
    vala = best_val(x)
    valb = best_val(y)
    if vala > valb:
        return 1
    if valb > vala:
        return -1
    for ca, cb in zip(x, y):
        na = to_num2(ca)
        nb = to_num2(cb)
        if na > nb:
            return 1
        if nb > na:
            return -1
    return 0


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
    pairs = []
    for line in data:
        asd = line.split(" ")
        bid = int(asd[1])
        pairs.append((asd[0], bid))
    for ini in ints:
        pass
    sortedDict = sorted(pairs, key=cmp_to_key(compare))
    for i, a in enumerate(sortedDict):
        ans += (i + 1) * a[1]
    print(len(pairs), len(set([x[0] for x in pairs])))

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
    pairs = []
    for line in data:
        asd = line.split(" ")
        bid = int(asd[1])
        pairs.append((asd[0], bid))
    for ini in ints:
        pass
    sortedDict = sorted(pairs, key=cmp_to_key(compare2))
    for i, a in enumerate(sortedDict):
        ans += (i + 1) * a[1]
    print(len(pairs), len(set([x[0] for x in pairs])))
    return ans


def main():
    day = 7
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
