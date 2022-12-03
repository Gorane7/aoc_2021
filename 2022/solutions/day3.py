from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def solve1(data):

    # first = map_lines(data[:1], [int], ",")
    parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed = my_map(parsed, lambda x: x)

    # SOLUTION
    l = []
    d = {}
    n = 0
    s = ""
    hs = set()
    ans = 0
    tot = LETTERS + UPPER_LETTERS
    for line in parsed:
        ss = len(line) // 2
        common = set(line[:ss]).intersection(line[ss:])
        for c in common:
            ans += tot.index(c) + 1

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
    parsed = map_lines(data, [str])
    ans = 0
    tot = LETTERS + UPPER_LETTERS
    for i in range(len(parsed) // 3):
        a = parsed[i * 3]
        b = parsed[i * 3 + 1]
        c = parsed[i * 3 + 2]
        common = set(a).intersection(set(b)).intersection(set(c))
        for c in common:
            ans += tot.index(c) + 1
    return ans


def main():
    day = 3
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
