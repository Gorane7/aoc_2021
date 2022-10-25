from main import *


def solve1(dat):
    data = dat["data"]
    levels = [[int(x) for x in y] for y in data]
    flashed = [[False for _ in range(10)] for _ in range(10)]
    flashes = 0
    for i in range(100):
        for y in range(len(levels)):
            for x in range(len(levels[y])):
                levels[y][x] += 1
        had_flashes = True
        while had_flashes:
            had_flashes = False
            for y in range(len(levels)):
                for x in range(len(levels[y])):
                    if levels[y][x] > 9 and not flashed[y][x]:
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                if dy + y >= 0 and dy + y < 10 and dx + x >= 0 and dx + x < 10:
                                    levels[y + dy][x + dx] += 1
                        had_flashes = True
                        flashed[y][x] = True
                        flashes += 1
        for y in range(len(flashed)):
            for x in range(len(flashed[y])):
                if flashed[y][x]:
                    levels[y][x] = 0
                    flashed[y][x] = False
    return flashes


def solve2(dat):
    data = dat["data"]
    levels = [[int(x) for x in y] for y in data]
    flashed = [[False for _ in range(10)] for _ in range(10)]
    i = 0
    while True:
        flashes = 0
        i += 1
        for y in range(len(levels)):
            for x in range(len(levels[y])):
                levels[y][x] += 1
        had_flashes = True
        while had_flashes:
            had_flashes = False
            for y in range(len(levels)):
                for x in range(len(levels[y])):
                    if levels[y][x] > 9 and not flashed[y][x]:
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                if dy + y >= 0 and dy + y < 10 and dx + x >= 0 and dx + x < 10:
                                    levels[y + dy][x + dx] += 1
                        had_flashes = True
                        flashed[y][x] = True
                        flashes += 1
        for y in range(len(flashed)):
            for x in range(len(flashed[y])):
                if flashed[y][x]:
                    levels[y][x] = 0
                    flashed[y][x] = False
        if flashes == 100:
            return i


def main():
    day = 11
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
