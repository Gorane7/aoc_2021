from main import *
import shelve


def solve1(data):
    # SOLUTION
    # first = map_lines(data[:1], [int], ",")
    # parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    # print(data)
    # print(parsed)
    # print(first if "first" in dir() else None)
    # END PARSING
    ans = 0
    this = 0
    for dat in data:
        if dat == "":
            ans = max(ans, this)
            this = 0
        else:
            this += int(dat)
    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()

    return ans


def solve2(dat):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    all = []
    this = 0
    for dat in data:
        if dat == "":
            all.append(this)
            this = 0
        else:
            this += int(dat)
    all.append(this)
    all.sort()

    return sum(all[-3:])


def main():
    day = 1
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1 = solve1(data)
    ans2 = solve2(data)
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
