from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def get_loc_dict(tree, loc):
    for a in loc:
        if a not in tree.keys():
            tree[a] = {}
        tree = tree[a]
    return tree


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
    loc = []
    loc_tree = {}
    while i < len(data):
        spl = data[i].split(" ")
        if data[i][0] == "$":
            if spl[1] == "cd":
                if spl[2] == "/":
                    loc = []
                elif spl[2] == "..":
                    loc.pop()
                else:
                    loc.append(spl[2])
            elif spl[1] == "ls":
                i += 1
                while i < len(data) and data[i][0] != "$":
                    spl = data[i].split(" ")
                    if spl[0] == "dir":
                        if spl[1] not in get_loc_dict(loc_tree, loc).keys():
                            get_loc_dict(loc_tree, loc)[spl[1]] = {}
                    else:
                        if spl[1] not in get_loc_dict(loc_tree, loc).keys():
                            get_loc_dict(loc_tree, loc)[spl[1]] = int(spl[0])
                    i += 1
                i -= 1
        else:
            pass
        i += 1
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
    small_files = []
    find_small_files_1(loc_tree, small_files)
    return sum(small_files)

def find_small_files_1(loc_tree, small_files):
    total_size = 0
    if isinstance(loc_tree, dict):
        for key, value in loc_tree.items():
            total_size += find_small_files_1(value, small_files)
    else:
        return loc_tree
    if total_size < 100000:
        small_files.append(total_size)
    loc_tree["total size"] = total_size
    return total_size


def find_small_files_2(loc_tree, small_files):
    total_size = 0
    if isinstance(loc_tree, dict):
        for key, value in loc_tree.items():
            total_size += find_small_files_2(value, small_files)
    else:
        return loc_tree
    small_files.append(total_size)
    loc_tree["total size"] = total_size
    return total_size


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    loc = []
    loc_tree = {}
    i = 0
    while i < len(data):
        spl = data[i].split(" ")
        if data[i][0] == "$":
            if spl[1] == "cd":
                if spl[2] == "/":
                    loc = []
                elif spl[2] == "..":
                    loc.pop()
                else:
                    loc.append(spl[2])
            elif spl[1] == "ls":
                i += 1
                while i < len(data) and data[i][0] != "$":
                    spl = data[i].split(" ")
                    if spl[0] == "dir":
                        if spl[1] not in get_loc_dict(loc_tree, loc).keys():
                            get_loc_dict(loc_tree, loc)[spl[1]] = {}
                    else:
                        if spl[1] not in get_loc_dict(loc_tree, loc).keys():
                            get_loc_dict(loc_tree, loc)[spl[1]] = int(spl[0])
                    i += 1
                i -= 1
        else:
            pass
        i += 1
    small_files = []
    find_small_files_2(loc_tree, small_files)
    best = 99999999999999999
    for file in small_files:
        if file < 30000000 - (70000000 - 47052440):
            continue
        best = min(file, best)
    return best


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


if __name__ == '__main__':
    main()
