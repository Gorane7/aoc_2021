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
    i = 0
    s = ""
    d = {}
    u = set()
    l = []
    ans = 0
    for line in data:
        a, b = line.split(",")
        a0, a1 = a.split("-")
        b0, b1 = b.split("-")
        a0, a1, b0, b1 = int(a0), int(a1), int(b0), int(b1)
        a = [i for i in range(a0, a1 + 1)]
        b = [i for i in range(b0, b1 + 1)]
        comb = set(a).intersection(b)
        if len(comb) > 0:
            ans += 1
        # ans += a1 >= b1 and a0 <= b0 or b1 >= a1 and b0 <= a0

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
        a, b = line.split(",")
        a0, a1 = a.split("-")
        b0, b1 = b.split("-")
        a0, a1, b0, b1 = int(a0), int(a1), int(b0), int(b1)
        ans += a1 >= b1 and a0 <= b0 or b1 >= a1 and b0 <= a0
    return ans


def main():
    day = 4
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
