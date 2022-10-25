from main import *


def solve1(dat):
    data = dat["data"]
    data = [[x for x in row] for row in data]
    i = 0
    moves = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
    while True:
        # print("\n".join(["".join(row) for row in data]))
        # print()
        i += 1
        amount_moved = 0
        for y, row in enumerate(data):
            for x, value in enumerate(row):
                if value == ".":
                    continue
                if value == ">":
                    moves[y][x] = row[(x + 1) % len(row)] == "."
        for y, row in enumerate(data):
            for x, value in enumerate(row):
                if moves[y][x]:
                    amount_moved += 1
                    moves[y][x] = False
                    row[(x + 1) % len(row)] = ">"
                    row[x] = "."
        for y, row in enumerate(data):
            for x, value in enumerate(row):
                if value == ".":
                    continue
                if value == "v":
                    moves[y][x] = data[(y + 1) % len(data)][x] == "."
        for y, row in enumerate(data):
            for x, value in enumerate(row):
                if moves[y][x]:
                    amount_moved += 1
                    moves[y][x] = False
                    data[(y + 1) % len(data)][x] = "v"
                    row[x] = "."
        if amount_moved == 0:
            break
    return i


def solve2(dat):
    data = dat["data"]
    return 0


def main():
    day = 25
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
