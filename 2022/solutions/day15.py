from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import time

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
        # print(f"Sensor: {s}, Becaon: {b}, Dist: {d}")

    # -389916 1188862

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    print(ans)
    return ans


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    cannot = set()

    for ini in ints:
        s = (ini[0], ini[1])
        b = (ini[2], ini[3])
        d = abs(s[0] - b[0]) + abs(s[1] - b[1])
        ini.append(d)
        # print(f"Sensor: {s}, Becaon: {b}, Dist: {d}")
    # cur_size = 21
    cur_size = 4000001
    total = cur_size * cur_size
    last_time = time.time()
    c = 0
    i = 0
    while i < total:
        c += 1
        if c % 100000 == 0:
            if time.time() - last_time > 1:
                print(f"{100 * i / total}%")
                last_time = time.time()
        x = i % cur_size
        y = i // cur_size
        found = True
        for ini in ints:
            d = abs(x - ini[0]) + abs(y - ini[1])
            if d <= ini[4]:
                found = False
                diff = abs(ini[1] - y)
                dx = ini[4] - diff
                new_x = ini[0] + dx
                new_x = min(cur_size - 2, new_x)
                # print(f"Location {x, y} has problem with sensor {ini[0], ini[1]}, ydiff is {diff}, xdiff is {dx}, can move forward {new_x}")
                i += max(1, (new_x - x) - 3)
                # i += 1
                break
        if found:
            print(x, y)
            break
    return x * (cur_size - 1) + y


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
