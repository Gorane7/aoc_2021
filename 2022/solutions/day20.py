from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


class Number:
    def __init__(self, value, index):
        self.val = value
        self.index = index


def find_index(listi, ind):
    print(ind)
    for i, val in enumerate(listi):
        if val.index == ind:
            return val, i


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
    orr = [Number(x[0], i) for i, x in enumerate(ints)]
    for i in range(5000):
        target, ind = find_index(orr, i)
        # print([x.val for x in orr])
        # print(f"Moving {target.val}")
        if target.val > 0:
            for j in range(ind, ind + target.val):
                if target.val > 0:
                    orr[j % len(orr)], orr[(j + 1) % len(orr)] = orr[(j + 1) % len(orr)], orr[j % len(orr)]
        else:
            for j in range(ind, ind + target.val, -1):
                if target.val > 0:
                    orr[j % len(orr)], orr[(j + 1) % len(orr)] = orr[(j + 1) % len(orr)], orr[j % len(orr)]
                elif target.val < 0:
                    orr[j % len(orr)], orr[(j - 1) % len(orr)] = orr[(j - 1) % len(orr)], orr[j % len(orr)]
    counter = -1
    total = 0
    curr = 0
    print([x.val for x in orr])
    while True:
        if counter == -1:
            if orr[curr % len(orr)].val == 0:
                counter = 1
            curr += 1
            continue
        if counter in [1000, 2000, 3000]:
            total += orr[(curr % len(orr))].val
            print(orr[(curr % len(orr))].val)
        curr += 1
        counter += 1
        if counter > 3000:
            break

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return total


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    ints = [extract_ints(x) for x in data]
    # first = map_lines(data[:1], [int], ",")
    parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed = my_map(parsed, lambda x: x)

    # SOLUTION HERE
    dekey = 811589153
    orr = [Number(x[0] * dekey, i) for i, x in enumerate(ints)]
    for i in range(10):
        leng = 7
        for k in range(leng):
            target, ind = find_index(orr, k)
            valu = target.val
            if valu > 0:
                valu = valu % leng
            if valu < 0:
                valu += leng * (abs(valu) // leng)
            if valu > 0:
                for j in range(ind, ind + valu):
                    if valu > 0:
                        orr[j % len(orr)], orr[(j + 1) % len(orr)] = orr[(j + 1) % len(orr)], orr[j % len(orr)]
            else:
                for j in range(ind, ind + valu, -1):
                    if valu > 0:
                        orr[j % len(orr)], orr[(j + 1) % len(orr)] = orr[(j + 1) % len(orr)], orr[j % len(orr)]
                    elif valu < 0:
                        orr[j % len(orr)], orr[(j - 1) % len(orr)] = orr[(j - 1) % len(orr)], orr[j % len(orr)]
    counter = -1
    total = 0
    curr = 0
    print([x.val for x in orr])
    print(len(orr))
    while True:
        if counter == -1:
            if orr[curr % len(orr)].val == 0:
                counter = 1
            curr += 1
            continue
        if counter in [1000, 2000, 3000]:
            total += orr[(curr % len(orr))].val
            print(orr[(curr % len(orr))].val)
        curr += 1
        counter += 1
        if counter > 3000:
            break
    return total




def main():
    day = 20
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    # ans1 = solve1([x for x in data])
    ans2 = solve2([x for x in data])
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
