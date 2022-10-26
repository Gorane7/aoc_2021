from main import *


def solve1(data):
    dat = data["data"]
    # print(dat)
    x = 0
    y = 0
    for line in dat:
        sp = line.split(" ")
        if sp[0] == "forward":
            x += int(sp[1])
        elif sp[0] == "down":
            y += int(sp[1])
        else:
            y -= int(sp[1])
    return y * x


def solve2(data):
    dat = data["data"]
    x = 0
    y = 0
    aim = 0
    for line in dat:
        sp = line.split(" ")
        if sp[0] == "forward":
            x += int(sp[1])
            y += int(sp[1]) * aim
        elif sp[0] == "down":
            aim += int(sp[1])
        else:
            aim -= int(sp[1])
    return y * x


def main():
    day = 2
    basic = [("...", "{string}")]
    ints = [("...", "{int}")]
    custom = [("...", "{string} {int}")]
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
