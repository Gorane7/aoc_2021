from main import *


def solve1(dat):
    data = dat["data"]
    points = []
    folds = []
    for line in data:
        split = line.split(",")
        if len(split) == 2:
            points.append((int(split[0]), int(split[1])))
        else:
            important = line.split(" ")[2].split("=")
            folds.append((important[0], int(important[1])))
    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])
    # print(max_x, max_y)
    cave_map = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(".")
        cave_map.append(row)
    for x, y, in points:
        cave_map[y][x] = "#"
    cave_map = fold(cave_map, folds[0])
    total = 0
    for row in cave_map:
        for value in row:
            total += value == "#"
    return total


def fold(cave_map, fold):
    dir = fold[0]
    at = fold[1]
    new_x = len(cave_map[0])
    new_y = len(cave_map)
    # print(fold)
    if dir == "y":
        new_y = at
    else:
        new_x = at
    # print(new_x, new_y)
    new_map = []
    for y in range(new_y):
        row = []
        for x in range(new_x):
            if cave_map[y][x] == "#":
                row.append("#")
                continue
            if dir == "x":
                if cave_map[y][at + (at - x)] == "#":
                    row.append("#")
                    continue
            if dir == "y":
                if cave_map[at + (at - y)][x] == "#":
                    row.append("#")
                    continue
            row.append(".")
        new_map.append(row)
    return new_map


def solve2(dat):
    data = dat["data"]
    points = []
    folds = []
    for line in data:
        split = line.split(",")
        if len(split) == 2:
            points.append((int(split[0]), int(split[1])))
        else:
            important = line.split(" ")[2].split("=")
            folds.append((important[0], int(important[1])))
    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])
    # print(max_x, max_y)
    cave_map = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(".")
        cave_map.append(row)
    for x, y, in points:
        cave_map[y][x] = "#"
    for my_fold in folds:
        cave_map = fold(cave_map, my_fold)
    for line in cave_map:
        pass
        # print("".join(line))


def main():
    day = 13
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
