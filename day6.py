from main import *


def solve1(dat):
    data = dat["data"]
    fishes = [0] * 9
    for fish in data[0].split(","):
        fishes[int(fish)] += 1
    for i in range(80):
        new = [0] * 9
        new[6] += fishes[0]
        new[8] += fishes[0]
        for j in range(1, 9):
            new[j - 1] += fishes[j]
        fishes = new
    return sum(fishes)


def solve2(dat):
    data = dat["data"]
    fishes = [0] * 9
    for fish in data[0].split(","):
        fishes[int(fish)] += 1
    for i in range(256):
        new = [0] * 9
        new[6] += fishes[0]
        new[8] += fishes[0]
        for j in range(1, 9):
            new[j - 1] += fishes[j]
        fishes = new
    return sum(fishes)


def main():
    day = 6
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
