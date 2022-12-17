from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def find_values(values, opened):
    total = 0
    for name, time in opened:
        total += time * values[name]
    return total


def find_best(graph, values, opened, time_left, location):
    if time_left < 2:
        return opened
    best = 0
    best_conf = None
    for oth in graph[location]:
        new_opened = {x for x in opened}
        if values[oth] > 0 and oth not in [x[0] for x in opened]:
            new_opened.add((oth, time_left - 2))
            temp = find_best(graph, values, new_opened, time_left - 2, oth)
            val = find_values(values, temp)
            if val > best:
                best = val
                best_conf = temp
        temp = find_best(graph, values, new_opened, time_left - 1, oth)
        val = find_values(values, temp)
        if val > best:
            best = val
            best_conf = temp
    return best_conf


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
    graph = {}
    values = {}
    for line in data:
        spl = line.split(" ")
        ori = spl[1]
        r = int(spl[4].split("=")[1].split(";")[0])
        other = " ".join(spl[9:]).split(", ")
        if ori not in graph.keys():
            graph[ori] = set()
        values[ori] = r
        for oth in other:
            graph[ori].add(oth)
            if oth not in graph.keys():
                graph[oth] = set()
            graph[oth].add(ori)
        print(ori, r, other)
    ans = find_best(graph, values, set(), 30, "AA")
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


def main():
    day = 16
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
