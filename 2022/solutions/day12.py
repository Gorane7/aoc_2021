from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
from queue import PriorityQueue

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


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
    grid = []
    start = None
    target = None
    for y, line in enumerate(data):
        grid.append([ch for ch in line])
        for x, ch in enumerate(line):
            if ch == "S":
                start = (x, y)
            if ch == "E":
                target = (x, y)
    queue = PriorityQueue()
    visited = set()
    rev_path = {}
    queue.put((0, start, None))
    el_map = {
        "E": "z",
        "S": "a"
    }
    while not queue.empty():
        # print(queue.qsize())
        dist, came_from, previous = queue.get()
        if grid[came_from[1]][came_from[0]] == "E":
            return dist
        if came_from in visited:
            continue
        visited.add(came_from)
        rev_path[came_from] = previous
        # print(dist, came_from, previous)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = came_from[0] + dx
            ny = came_from[1] + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            if (nx, ny) in visited:
                continue
            el_let = grid[ny][nx] if grid[ny][nx] in LETTERS else el_map[grid[ny][nx]]

            el_let_prev = grid[came_from[1]][came_from[0]] if grid[came_from[1]][came_from[0]] in LETTERS else el_map[grid[came_from[1]][came_from[0]]]
            # print(el_let, el_let_prev)
            if LETTERS.index(el_let) - LETTERS.index(el_let_prev) > 1:
                continue
            queue.put((dist + 1, (nx, ny), came_from))
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
    grid = []
    start = None
    target = None
    for y, line in enumerate(data):
        grid.append([ch for ch in line])
        for x, ch in enumerate(line):
            if ch == "S":
                start = (x, y)
            if ch == "E":
                target = (x, y)
    queue = PriorityQueue()
    visited = set()
    rev_path = {}
    queue.put((0, start, None))
    el_map = {
        "E": "z",
        "S": "a"
    }
    while not queue.empty():
        # print(queue.qsize())
        dist, came_from, previous = queue.get()
        if grid[came_from[1]][came_from[0]] == "E":
            return dist
        if came_from in visited:
            continue
        visited.add(came_from)
        rev_path[came_from] = previous
        # print(dist, came_from, previous)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = came_from[0] + dx
            ny = came_from[1] + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            if (nx, ny) in visited:
                continue
            el_let = grid[ny][nx] if grid[ny][nx] in LETTERS else el_map[grid[ny][nx]]

            el_let_prev = grid[came_from[1]][came_from[0]] if grid[came_from[1]][came_from[0]] in LETTERS else el_map[grid[came_from[1]][came_from[0]]]
            # print(el_let, el_let_prev)
            if LETTERS.index(el_let) - LETTERS.index(el_let_prev) > 1:
                continue
            queue.put((dist + 1 if el_let_prev != "a" else 1, (nx, ny), came_from))


def main():
    day = 12
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
