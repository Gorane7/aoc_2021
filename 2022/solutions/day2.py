from main import *
import shelve


def solve1(data):

    # first = map_lines(data[:1], [int], ",")
    parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])

    # SOLUTION
    l = []
    d = {}
    n = 0
    s = ""
    hs = set()
    ans = 0
    ss = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    ws = {
        "XA": 3,
        "YB": 3,
        "ZC": 3,
        "XC": 6,
        "YA": 6,
        "ZB": 6
    }
    for line in parsed:
        ab = line[1] + line[0]
        ans += ss[line[1]]
        if ab in ws.keys():
            ans += ws[ab]

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
    parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])

    # SOLUTION
    l = []
    d = {}
    n = 0
    s = ""
    hs = set()
    ans = 0
    ws2 = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    ms2 = {
        "XA": 3,
        "XB": 1,
        "XC": 2,
        "YA": 1,
        "YB": 2,
        "YC": 3,
        "ZA": 2,
        "ZB": 3,
        "ZC": 1
    }
    for line in parsed:
        ans += ws2[line[1]]
        ans += ms2[line[1] + line[0]]
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
