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
    #data   = my_map(data, lambda x: [int(a) for a in x.split(" ")])
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

    for line in data:
        
        asd = line.split(": ")
        idd = int(asd[0].split(" ")[-1])
        works = True
        for astep in asd[1].split("; "):
            allowed = {
                "red": 12,
                "green": 13,
                "blue": 14
            }
            for step in astep.split(", "):
                aa = step.split(" ")
                amount = int(aa[0])
                colour = aa[1]
                allowed[colour] -= amount
            
            for colour, amount in allowed.items():
                if amount < 0:
                    works = False
        if works:
            ans += idd
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
    for line in data:
        asd = line.split(": ")
        idd = int(asd[0].split(" ")[-1])
        globala = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for astep in asd[1].split("; "):
            allowed = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for step in astep.split(", "):
                aa = step.split(" ")
                amount = int(aa[0])
                colour = aa[1]
                allowed[colour] += amount
            for key, val in allowed.items():
                globala[key] = max(val, globala[key])
        ans += globala["green"] * globala["blue"] * globala["red"]
    return ans


def main():
    day = 2
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
