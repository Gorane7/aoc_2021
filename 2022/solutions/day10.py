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
    ans = 1
    values = []
    picture = [["."] * 40 for _ in range(6)]
    for line in data:
        if line == "noop":
            values.append(ans)
        else:
            spl = line.split(" ")
            a = int(spl[1])
            values.append(ans)
            values.append(ans)
            ans += a

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
    targets = [20, 60, 100, 140, 180, 220]
    total = 0
    for tar in targets:
        total += tar * values[tar - 1]
    return total


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    ans = 1
    i = 0
    values = []
    picture = [["."] * 40 for _ in range(6)]
    for line in data:
        if line == "noop":
            values.append(ans)
            if abs(i % 40 - values[-1]) <= 1:
                picture[(i - 1) // 40][(i - 1) % 40] = "#"
            i += 1
        else:
            spl = line.split(" ")
            a = int(spl[1])
            values.append(ans)

            if abs(i % 40 - values[-1]) <= 1:
                picture[(i - 1) // 40][(i - 1) % 40] = "#"
            i += 1
            values.append(ans)

            if abs(i % 40 - values[-1]) <= 1:
                picture[(i - 1) // 40][(i - 1) % 40] = "#"
            i += 1
            ans += a
    for row in picture:
        print("".join(row))
    print(values)


def main():
    day = 10
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
