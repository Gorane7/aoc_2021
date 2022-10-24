from main import *


def solve1(dat):
    data = dat["data"]
    maps = []
    for line in data:
        row = []
        for chara in line:
            row.append(int(chara))
        maps.append(row)
    amount = 0
    locs = []
    total = 0
    for y, row in enumerate(maps):
        for x, value in enumerate(row):
            if is_low_point(x, y, maps):
                total += value + 1
    return total


def is_low_point(x, y, maps):
    is_ = True
    tar = maps[y][x]
    if x != 0:
        if maps[y][x - 1] <= tar:
            return False
    if y != 0:
        if maps[y - 1][x] <= tar:
            return False
    if x != len(maps[0]) - 1:
        if maps[y][x + 1] <= tar:
            return False
    if y != len(maps) - 1:
        if maps[y + 1][x] <= tar:
            return False
    return True



def solve2(dat):
    data = dat["data"]
    maps = []
    data_map = {}
    points_to = {}
    for y, line in enumerate(data):
        row = []
        for x, chara in enumerate(line):
            row.append(int(chara))
            data_map[(x, y)] = {(x, y)}
            points_to[(x, y)] = [(x, y)]
        maps.append(row)
    amount = 0
    locs = []
    total = 0
    for y, row in enumerate(maps):
        for x, value in enumerate(row):
            points_to[(x, y)] = flows_to(x, y, maps)
    for y, row in enumerate(maps):
        for x, value in enumerate(row):
            been = set()
            flow(x, y, x, y, data_map, points_to, maps, been, -1, -1)

    needed = len(maps) * len(maps[0])
    have = 0
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            have += 1
            # print(f"{have / needed}")
            count = 0
            for y1 in range(len(maps)):
                for x1 in range(len(maps[0])):
                    if (x, y) in data_map[(x1, y1)]:
                        count += 1
            if count > 1:
                for y1 in range(len(maps)):
                    for x1 in range(len(maps[0])):
                        if (x, y) in data_map[(x1, y1)]:
                            # data_map[(x1, y1)].remove((x, y))
                            pass

    lens = []
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            # if (x, y)
            # print(f"{x}, {y} size is {len(data_map[(x, y)])}: {data_map[(x, y)]}")
            lens.append(len([qwe for qwe in data_map[(x, y)] if maps[qwe[1]][qwe[0]] != 9]))
    lens = sorted(lens, reverse=True)
    # print(lens)
    # print(sum(lens))
    # print()
    # pretty_print(2, 2, data_map, len(maps[0]), len(maps), maps)
    return lens[0] * lens[1] * lens[2]


def pretty_print(x, y, data, x_size, y_size, raw_data):
    for yi in range(y_size):
        line = ""
        for xi in range(x_size):
            if (xi, yi) in data[(x, y)]:
                line += str(raw_data[yi][xi])
            else:
                line += " "
        # print(line)


def flow(orig_x, orig_y, x, y, data_map, points_to, maps, been, mem_x, mem_y):
    # print((4, 1) in data_map.keys())
    if (x, y) in been:
        # data_map[(x, y)].remove((orig_x, orig_y))
        return
    been.add((x, y))
    for target in points_to[(x, y)]:
        # print(f"{x}, {y}")
        if (orig_x, orig_y) in data_map[(x, y)]:
            data_map[(x, y)].remove((orig_x, orig_y))
        data_map[target].add((orig_x, orig_y))
        # print(f"{orig_x}, {orig_y} flows from {x}, {y} to {target}")
        if target != (x, y):
            flow(orig_x, orig_y, target[0], target[1], data_map, points_to, maps, been, x, y)



def flows_to(x, y, maps):
    is_ = True
    orig = maps[y][x]
    min_value = maps[y][x]
    min_locs = [(x, y)]
    changed = False
    if x != 0:
        if maps[y][x - 1] <= orig:
            if not changed:
                min_locs = []
                changed = True
            min_locs.append((x - 1, y))
    if y != 0:
        if maps[y - 1][x] <= orig:
            if not changed:
                min_locs = []
                changed = True
            min_locs.append((x, y - 1))
    if x != len(maps[0]) - 1:
        if maps[y][x + 1] <= orig:
            if not changed:
                min_locs = []
                changed = True
            min_locs.append((x + 1, y))
    if y != len(maps) - 1:
        if maps[y + 1][x] <= orig:
            if not changed:
                min_locs = []
                changed = True
            min_locs.append((x, y + 1))
    return min_locs


def main():
    day = 9
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
