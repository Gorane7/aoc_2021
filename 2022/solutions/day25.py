from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def get_next(val):
    if val == "1":
        return "2"
    if val == "0":
        return "1"
    if val == "-":
        return "0"
    if val == "=":
        return "-"
    if val == "2":
        return "3"


def solve1(data):

    # ints = [extract_ints(x) for x in data]
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
    valmap = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2
    }
    for line in data:
        for i, ch in enumerate(line[::-1]):
            ans += 5**i * valmap[ch]
        pass

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    acans = ""
    while ans > 0:
        acans += str(ans % 5)
        ans = ans // 5
    acans = [ch for ch in acans[::-1]]
    while "3" in acans or "4" in acans:
        i = 0
        while i < len(acans):
            if acans[i] == "3":
                acans[i] = "="
                acans[i - 1] = get_next(acans[i - 1])
            if acans[i] == "4":
                acans[i] = "-"
                acans[i - 1] = get_next(acans[i - 1])
            i += 1
    return "".join(acans)


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE


def main():
    day = 25
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
