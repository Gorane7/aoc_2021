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
    stacks = [
        "RNPG",
        "TJBLCSVH",
        "TDBMNL",
        "RVPSB",
        "GCQSWMVH",
        "WQSCDBJ",
        "FQL",
        "WMHTDLFV",
        "LPBVMJF"
    ]
    stacks = [[x for x in line] for line in stacks]
    for line in data[10:]:
        a = line.split(" ")
        am = int(a[1])
        f = int(a[3])
        t = int(a[5])
        for i in range(am):
            stacks[t - 1].append(stacks[f - 1].pop())

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return "".join([x[-1] for x in stacks])


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    stacks = [
        "RNPG",
        "TJBLCSVH",
        "TDBMNL",
        "RVPSB",
        "GCQSWMVH",
        "WQSCDBJ",
        "FQL",
        "WMHTDLFV",
        "LPBVMJF"
    ]
    stacks = [[x for x in line] for line in stacks]
    for line in data[10:]:
        a = line.split(" ")
        am = int(a[1])
        f = int(a[3])
        t = int(a[5])
        stacks[t-1] = stacks[t-1] + stacks[f - 1][-am:]
        stacks[f - 1] = stacks[f - 1][:-am]

    # SOLUTION HERE
    return "".join([x[-1] for x in stacks])


def main():
    day = 5
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
