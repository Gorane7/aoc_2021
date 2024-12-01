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
    boxes = []
    y = 0
    for line in data:
        ni = []
        for i, ch in enumerate(line):
            if ch in NUMBERS:
                ni.append(i)
        last = None
        start = None
        nn = None
        ni2 = []
        for i in ni:
            if last is None:
                last = i
                start = i
                nn = i
                continue
            if last + 1 == i:
                nn = i
                last = i
                continue
            ni2.append((start, nn))
            last = i
            start = i
            nn = i
        if start is not None:
            ni2.append((start, nn))
        for a, b in ni2:
            works = False
            for i in range(a - 1, b + 2):
                try:
                    if data[y - 1][i] != "." and data[y - 1][i] not in NUMBERS:
                        works = True
                except:
                    pass
                try:
                    
                    if data[y + 1][i] != "." and data[y + 1][i] not in NUMBERS:
                        works = True
                except:
                    pass
            try:
                
                if data[y][a - 1] != "." and data[y][a - 1] not in NUMBERS:
                    works = True
            except:
                pass
            try:
                
                if data[y][b + 1] != "." and data[y][b + 1] not in NUMBERS:
                    works = True
            except:
                pass
            if works:
                ans += int(line[a:b + 1])
        #print(ni2)
        y += 1

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
    i = 0
    s = ""
    d = {}
    u = set()
    l = []
    ans = 0
    boxes = []
    y = 0
    gears = {}
    for line in data:
        ni = []
        for i, ch in enumerate(line):
            if ch in NUMBERS:
                ni.append(i)
        last = None
        start = None
        nn = None
        ni2 = []
        for i in ni:
            if last is None:
                last = i
                start = i
                nn = i
                continue
            if last + 1 == i:
                nn = i
                last = i
                continue
            ni2.append((start, nn))
            last = i
            start = i
            nn = i
        if start is not None:
            ni2.append((start, nn))
        for a, b in ni2:
            works = False
            gear_at = None
            for i in range(a - 1, b + 2):
                try:
                    if data[y - 1][i] != "." and data[y - 1][i] not in NUMBERS:
                        works = True
                        if data[y - 1][i] == "*":
                            gear_at = (y - 1, i)
                except:
                    pass
                try:
                    if data[y + 1][i] != "." and data[y + 1][i] not in NUMBERS:
                        works = True
                        if data[y + 1][i] == "*":
                            gear_at = (y + 1, i)
                except:
                    pass
            try:
                if data[y][a - 1] != "." and data[y][a - 1] not in NUMBERS:
                    works = True
                    if data[y][a - 1] == "*":
                        gear_at = (y, a - 1)
            except:
                pass
            try:
                if data[y][b + 1] != "." and data[y][b + 1] not in NUMBERS:
                    works = True
                    if data[y][b + 1] == "*":
                        gear_at = (y, b + 1)
            except:
                pass
            if works:
                ans += int(line[a:b + 1])
                if gear_at is not None:
                    if gear_at not in gears.keys():
                        gears[gear_at] = []
                    gears[gear_at].append(int(line[a:b + 1]))
        #print(ni2)
        y += 1
    ans = 0
    for gear, nums in gears.items():
        if len(nums) == 2:
            ans += nums[0] * nums[1]
    return ans


def main():
    day = 3
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
