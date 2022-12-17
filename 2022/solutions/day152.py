from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def solve1(data):

    ints = [extract_ints(x) for x in data]
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
        pass
    tar = 2000000
    cannot = set()

    for ini in ints:
        s = (ini[0], ini[1])
        b = (ini[2], ini[3])
        d = abs(s[0] - b[0]) + abs(s[1] - b[1])
        ini.append(d)
        print(f"Sensor: {s}, Becaon: {b}, Dist: {d}")
    total = 4000000 * 4000000
    while i < total:
        if i % 10000000 == 0:
            print(f"{100 * i / total}%")
        x = i // 4000000
        y = i % 4000000
        found = True
        for ini in ints:
            d = abs(x - ini[0]) + abs(y - ini[1])
            if d <= ini[4]:
                found = False
                diff = abs(ini[1] - y)
                dx = ini[4] - diff
                new_x = ini[0] + dx
                new_x = max(4000000, new_x)
                i += (new_x - x) - 1
                break
        if found:
            print(x, y)
            break


        i += 1

    # -389916 1188862

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


def main():
    day = 15
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
