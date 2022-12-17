from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import time

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def get_max_height(columns):
    col_h = len(columns[0])
    i = 0
    for i in range(col_h):
        found = False
        for y in range(len(columns)):
            if columns[y][col_h - i - 1]:
                found = True
                break
        if found:
            break
    return col_h - i


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
    columns = [[] for _ in range(7)]
    jc = 0
    rc = 0
    rpc = 0
    current = None
    rocks = [
        {(0, 0), (1, 0), (2, 0), (3, 0)},
        {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
        {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
        {(0, 0), (0, 1), (0, 2), (0, 3)},
        {(0, 0), (0, 1), (1, 0), (1, 1)}
    ]
    start = time.time()
    start_configurations = {}
    max_amount = 0
    while rc < 2022:
        if current is None:
            top_look = []
            height = get_max_height(columns)
            lvl = height - 1
            while True:
                am = 0
                for y in range(7):
                    if lvl == -1:
                        top_look.append("#")
                        am += 1
                        continue
                    if columns[y][lvl]:
                        top_look.append("#")
                        am += 1
                    else:
                        top_look.append(".")
                if am == 7:
                    break
                lvl -= 1
            top_look = "".join(top_look)
            key = (rpc, jc, top_look)
            if key not in start_configurations.keys():
                start_configurations[key] = 0
            start_configurations[key] += 1
            if start_configurations[key] > max_amount:
                max_amount = start_configurations[key]
            # print(f"Setting new at height {get_max_height(columns)}")
            # print(f"Rock {rc} starts falling")
            current = (2, get_max_height(columns) + 3, rocks[rpc])
            rpc = (rpc + 1) % len(rocks)

        if data[0][jc] == "<":
            # print("Pushing left")
            new_x = current[0] - 1
        else:
            # print("Pushing right")
            new_x = current[0] + 1
        is_ok = True
        for tx, ty in current[2]:
            nx, ny = tx + new_x, ty + current[1]
            while ny >= len(columns[0]):
                for col in columns:
                    col.append(False)
            if nx < 0 or ny < 0 or nx >= len(columns) or columns[nx][ny]:
                is_ok = False
        # print(f"A ok was {is_ok}")
        if is_ok:
            current = (new_x, current[1], current[2])
        jc = (jc + 1) % len(data[0])

        new_y = current[1] - 1
        is_ok = True
        for tx, ty in current[2]:
            nx, ny = tx + current[0], ty + new_y
            while ny >= len(columns[0]):
                for col in columns:
                    col.append(False)
            if nx < 0 or ny < 0 or nx >= len(columns) or columns[nx][ny]:
                # print(f"False with {tx, ty}, which was at {nx, ny}")
                is_ok = False
        # print(f"B ok was {is_ok}")
        if is_ok:
            current = (current[0], new_y, current[2])
        else:
            # print("Hit ground")
            # print(columns)
            for tx, ty in current[2]:
                nx, ny = tx + current[0], ty + current[1]
                columns[nx][ny] = True
            rc += 1
            current = None
    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return get_max_height(columns)


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    ans = 0
    columns = [[] for _ in range(7)]
    jc = 0
    rc = 0
    rpc = 0
    current = None
    rocks = [
        {(0, 0), (1, 0), (2, 0), (3, 0)},
        {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
        {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
        {(0, 0), (0, 1), (0, 2), (0, 3)},
        {(0, 0), (0, 1), (1, 0), (1, 1)}
    ]
    start = time.time()
    start_configurations = {}
    max_amount = 0
    last_key = None
    key_map = {}
    key_heights = {}
    while rc < 1000000000000:
        if current is None:
            top_look = []
            height = get_max_height(columns)
            lvl = height - 1
            while True:
                am = 0
                for y in range(7):
                    if lvl == -1:
                        top_look.append("#")
                        am += 1
                        continue
                    if columns[y][lvl]:
                        top_look.append("#")
                        am += 1
                    else:
                        top_look.append(".")
                if am == 7:
                    break
                lvl -= 1
            top_look = "".join(top_look)
            key = (rpc, jc, top_look)
            key_heights[key] = height
            if last_key is not None:
                key_map[last_key] = (key, height - key_heights[last_key])
            if key in key_map.keys():
                break
            last_key = key
            if key not in start_configurations.keys():
                start_configurations[key] = 0
            start_configurations[key] += 1
            if start_configurations[key] > max_amount:
                max_amount = start_configurations[key]
            # print(f"Setting new at height {get_max_height(columns)}")
            # print(f"Rock {rc} starts falling")
            current = (2, get_max_height(columns) + 3, rocks[rpc])
            rpc = (rpc + 1) % len(rocks)

        if data[0][jc] == "<":
            # print("Pushing left")
            new_x = current[0] - 1
        else:
            # print("Pushing right")
            new_x = current[0] + 1
        is_ok = True
        for tx, ty in current[2]:
            nx, ny = tx + new_x, ty + current[1]
            while ny >= len(columns[0]):
                for col in columns:
                    col.append(False)
            if nx < 0 or ny < 0 or nx >= len(columns) or columns[nx][ny]:
                is_ok = False
        # print(f"A ok was {is_ok}")
        if is_ok:
            current = (new_x, current[1], current[2])
        jc = (jc + 1) % len(data[0])

        new_y = current[1] - 1
        is_ok = True
        for tx, ty in current[2]:
            nx, ny = tx + current[0], ty + new_y
            while ny >= len(columns[0]):
                for col in columns:
                    col.append(False)
            if nx < 0 or ny < 0 or nx >= len(columns) or columns[nx][ny]:
                # print(f"False with {tx, ty}, which was at {nx, ny}")
                is_ok = False
        # print(f"B ok was {is_ok}")
        if is_ok:
            current = (current[0], new_y, current[2])
        else:
            # print("Hit ground")
            # print(columns)
            for tx, ty in current[2]:
                nx, ny = tx + current[0], ty + current[1]
                columns[nx][ny] = True
            rc += 1
            current = None
    hd = 0
    t_key = key
    c = 0
    while hd == 0 or key != t_key:
        c += 1
        hd += key_map[t_key][1]
        t_key = key_map[t_key][0]
    left = 1000000000000 - rc
    full_steps = left // c
    rc += full_steps * c
    height += full_steps * hd
    while rc < 1000000000000:
        height += key_map[key][1]
        key = key_map[key][0]
        rc += 1
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
    picture = []
    # print(columns)
    for i in range(len(columns[0])):
        row = ""
        for y in range(7):
            row += ("#" if columns[y][i] else ".")
        picture.append(row)
    # print("\n".join(picture[::-1]))
    return height


def main():
    day = 17
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
