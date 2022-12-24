from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

from queue import PriorityQueue


def get_new_storms(storms, ylen, xlen):
    new_storms = set()
    dir_dir = {
        "v": (0, 1),
        "^": (0, -1),
        "<": (-1, 0),
        ">": (1, 0)
    }
    for x, y, dire in storms:
        dx, dy = dir_dir[dire]
        nx, ny = x + dx, y + dy
        if dire == "v":
            if ny == ylen - 1:
                ny = 1
        elif dire == "^":
            if ny == 0:
                ny = ylen - 2
        elif dire == "<":
            if nx == 0:
                nx = xlen - 2
        else:
            if nx == xlen - 1:
                nx = 1
        new_storms.add((nx, ny, dire))
    return new_storms


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
    x, y = 1, 0
    storms = set()
    for y in range(len(data)):
        data[y] = [ch for ch in data[y]]
        for x in range(len(data[y])):
            if data[y][x] in "v^<>":
                storms.add((x, y, data[y][x]))
    storms_at_times = {}
    storms_at_times[0] = storms
    q = PriorityQueue()
    q.put((0, 1, 0))
    visited = set()
    reached_times = 0
    goalx = 6
    goaly = 5
    goalx = 120
    goaly = 26
    goal_list = [(1, 0), (goalx, goaly)]
    while not q.empty():
        time_passed, x, y = q.get()
        print(time_passed, x, y)
        if time_passed + 1 not in storms_at_times.keys():
            storms_at_times[time_passed + 1] = get_new_storms(storms_at_times[time_passed], len(data), len(data[0]))
        if x == goalx and y == goaly:
            print("Found goal")
            if reached_times == 2:
                return time_passed
            goalx, goaly = goal_list[reached_times]
            reached_times += 1
            while not q.empty():
                q.get()
            q.put((time_passed, x, y))
            continue
        if (time_passed, x, y) in visited:
            continue
        visited.add((time_passed, x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(data[0]) or ny >= len(data) or data[ny][nx] == "#":
                continue
            collides = False
            for dire in "v^<>":
                if (nx, ny, dire) in storms_at_times[time_passed + 1]:
                    collides = True
                    break
            if collides:
                continue
            q.put((time_passed + 1, nx, ny))

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
    return ans


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE


def main():
    day = 24
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
