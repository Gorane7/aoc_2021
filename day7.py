from main import *


def solve1(dat):
    data = dat["data"]
    poss = [int(x) for x in data[0].split(",")]
    mini = min(poss)
    maxi = max(poss)
    best_fuel = 100000000000000000000000000000000
    for i in range(mini, maxi + 1):
        this_fuel = 0
        for pos in poss:
            this_fuel += abs(pos - i)
        if this_fuel < best_fuel:
            best_fuel = this_fuel
    return best_fuel

def get(i):
    ans = 0
    return i * (i + 1) // 2


def solve2(dat):
    data = dat["data"]
    poss = [int(x) for x in data[0].split(",")]
    mini = min(poss)
    maxi = max(poss)
    best_fuel = 100000000000000000000000000000000
    for i in range(mini, maxi + 1):
        this_fuel = 0
        for pos in poss:
            this_fuel += get(abs(pos - i))
        if this_fuel < best_fuel:
            best_fuel = this_fuel
    return best_fuel


def main():
    day = 7
    basic = [("...", "{string}")]
    ints = [("...", "{int}")]
    input_format = basic
    data = parse_input(day, input_format)
    if data["data"]:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1 = solve1(data)
    ans2 = solve2(data)
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
