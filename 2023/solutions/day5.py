from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def solve1(data):

    #ints     = [extract_ints(x) for x in data]
    # first  = map_lines(data[:1], [int], ",")
    parsed   = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed   = my_map(parsed, lambda x: x)
    data     = my_map(data, lambda x: x)
    #data    = my_map(data, lambda x: [int(a) for a in x.split(" ")])
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
    seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]
    maps = []
    index = 0
    cur_map = []
    for line in data[1:]:
        
        if not line:
            if cur_map:
                maps.append(cur_map)
                cur_map = []
            continue
        if "map" in line:
            continue
        #print([line])
        a, b, c = [int(x) for x in line.split(" ")]
        cur_map.append((a, b, c))
    if cur_map:
        maps.append(cur_map)
    #print(seeds)
    for m in maps:
        #print(m)
        new_seeds = []
        for seed in seeds:
            mapped = False
            for a, b, c in m:
                if seed >= b and seed < b + c:
                    new_seeds.append(a + seed - b)
                    mapped = True
                    break
            if not mapped:
                new_seeds.append(seed)
        seeds = new_seeds
        #print(seeds)



    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return min(seeds)


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    ans = 0
    seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]
    seeds = [(seeds[i * 2], seeds[i * 2 + 1]) for i in range(len(seeds) // 2)]
    total_length = sum([x[1] for x in seeds])
    min_seed = 99999999999999999999999

    maps = []
    index = 0
    cur_map = []
    for line in data[1:]:
        
        if not line:
            if cur_map:
                maps.append(cur_map)
                cur_map = []
            continue
        if "map" in line:
            continue
        #print([line])
        a, b, c = [int(x) for x in line.split(" ")]
        cur_map.append((a, b, c))
    if cur_map:
        maps.append(cur_map)
    #print(seeds)
    j = 0
    for start, length in seeds:
        for i in range(start, start + length):
            this_seed = start + i
            for m in maps:
                #print(m)
                for a, b, c in m:
                    if this_seed >= b and this_seed < b + c:
                        this_seed = a + this_seed - b
                        break
            min_seed = min(min_seed, this_seed)
            j += 1
            if j % 100000 == 0:
                print(f"{100 * j / total_length}% done")
    return min(seeds)


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

    testdata = parse_input(-1)
    if testdata:
        ans1t = solve1([x for x in testdata])
        ans2t = solve2([x for x in testdata])
        print(f"Answer a: {ans1}")
        print(f"Answer b: {ans2}")
        print(f"Test a: {ans1t}")
        print(f"Test b: {ans2t}")


if __name__ == '__main__':
    main()
