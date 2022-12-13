from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import functools

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if right < left:
            return 1
        return 0
    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return 0
        if len(left) == 0:
            return -1
        if len(right) == 0:
            return 1
        res = compare(left[0], right[0])
        if res != 0:
            return res
        return compare(left[1:], right[1:])
    if isinstance(left, int):
        return compare([left], right)
    return compare(left, [right])


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
    print(len(data))
    for i in range((len(data) + 1) // 3):
        left = eval(data[i * 3])
        right = eval(data[i * 3 + 1])
        result = compare(left, right)
        if result == -1:
            ans += i + 1
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
    packets = []
    packets.append([[2]])
    packets.append([[6]])
    for i in range((len(data) + 1) // 3):
        left = eval(data[i * 3])
        right = eval(data[i * 3 + 1])
        packets.append(left)
        packets.append(right)
    packets = sorted(packets, key=functools.cmp_to_key(compare))
    a = -1
    b = -1
    for i, packet in enumerate(packets):
        if packet == [[2]]:
            a = i + 1
        if packet == [[6]]:
            b = i + 1
    return a * b


def main():
    day = 13
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
