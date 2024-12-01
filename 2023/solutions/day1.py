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
    data   = my_map(data, lambda x: x)
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
    qwe = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    for line in data:
        a, b = 0, 0
        ai, bi = 999999999999999, -1
        asd = False
        i = 0
        for ch in line:
            if ch in NUMBERS:
                b = int(ch)
                bi = i
                if not asd:
                    a = int(ch)
                    ai = i
                    asd = True
            i += 1
        ans += a * 10 + b
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
    qwe = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    for line in data:
        a, b = 0, 0
        ai, bi = 999999999999999, -1
        asd = False
        i = 0
        for ch in line:
            if ch in NUMBERS:
                b = int(ch)
                bi = i
                if not asd:
                    a = int(ch)
                    ai = i
                    asd = True
            i += 1
        mini = 10000000000000
        minval = None
        maxi = -1
        maxval = None
        for val in qwe:
            try:
                zxc = line.find(val)
                zxcv = line.rfind(val)
            except:
                continue
            if zxc > -1 and zxc < mini:
                mini = zxc
                minval = qwe.index(val) + 1
            if zxcv > -1 and zxcv > maxi:
                maxi = zxcv
                maxval = qwe.index(val) + 1
        if mini < ai:
            a = minval
            ai = mini
        if maxi > bi:
            b = maxval
            bi = maxi
        ans += a * 10 + b
    return ans


def main():
    day = 1
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
    pass
    main()
