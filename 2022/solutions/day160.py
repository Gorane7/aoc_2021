from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
from queue import PriorityQueue

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

global all_dists
all_dists = {}


def find_values(values, opened):
    total = 0
    for name, time in opened:
        total += time * values[name]
    return total

def find_dists(values, loc, graph):
    global all_dists
    if loc in all_dists.keys():
        return all_dists[loc]
    paths = []
    for name, value in values:
        time, path = find_dist(loc, name, graph)
        paths.append((time, path, name, value))
    all_dists[loc] = paths
    return paths
    i, j = 0, 1
    while True:
        if j >= len(paths):
            i += 1
            j = i + 1
            if i >= len(paths):
                break
            continue
        a = paths[i]
        b = paths[j]
        if len(a[1]) < len(b[1]):
            if a[1] == b[1][:len(a[1])]:
                paths.pop(j)
                i, j = 0, 1
                continue
        elif len(b[1]) < len(a[1]):
            if b[1] == a[1][:len(b[1])]:
                paths.pop(i)
                i, j = 0, 1
                continue
        j += 1
    return paths


def find_dist(start, target, graph):
    queue = PriorityQueue()
    visited = set()
    from_dict = {}
    queue.put((0, start, None))
    while not queue.empty():
        dist, came_from, previous = queue.get()
        if came_from in visited:
            continue
        visited.add(came_from)
        from_dict[came_from] = previous
        if came_from == target:
            break
        for ne in graph[came_from]:
            queue.put((dist + 1, ne, came_from))
    path = []
    prev = target
    while prev is not None:
        path.append(prev)
        prev = from_dict[prev]
    return len(path), path[::-1]


def find_best(graph, values, opened, time_left, location, depth):
    best = find_values(values, opened)
    best_conf = opened
    for name, value in values.items():
        if depth < 1:
            print(name)
        time, path = find_dist(location, name, graph)
        if time >= time_left:
            continue
        if name in {x[0] for x in opened}:
            continue
        new_opened = {x for x in opened}
        new_opened.add((name, time_left - time))
        temp = find_best(graph, values, new_opened, time_left - time, name, depth + 1)
        val = find_values(values, temp)
        if val > best:
            best = val
            best_conf = temp
    return best_conf

def find_best_2(graph, values, opened, time_left, location, depth, bounds):
    val = find_values(values, opened)
    key1 = (location[0], location[1], location[2], location[3], "-".join(sorted([x[0] for x in opened])))
    key2 = (location[2], location[3], location[0], location[1], "-".join(sorted([x[0] for x in opened])))
    if key1 in bounds.keys() and bounds[key1][0] >= val and bounds[key1][2] >= time_left:
        # print("Optimized")
        return bounds[key1][1]
    if key2 in bounds.keys() and bounds[key2][0] >= val and bounds[key2][2] >= time_left:
        # print("Optimized")
        return bounds[key2][1]
    best = find_values(values, opened)
    best_conf = opened
    loc = location[0] if location[1] == 0 else location[2]
    other_loc = location[2] if location[1] == 0 else location[0]
    for time, path, name, value in find_dists(values.items(), loc, graph):
        if name == other_loc:
            continue
        if depth < 2:
            print(" " * 2 * (depth) + str(name))
        if time >= time_left:
            continue
        if name in {x[0] for x in opened}:
            continue
        new_opened = {x for x in opened}
        new_opened.add((name, time_left - time))
        time_spent = min(time, location[1] if location[1] != 0 else location[3])
        if location[1] == 0:
            new_loc = (name, time - time_spent, location[2], location[3] - time_spent)
        else:
            new_loc = (location[0], location[1] - time_spent, name, time - time_spent)
        temp = find_best_2(graph, values, new_opened, time_left - time_spent, new_loc, depth + 1, bounds)
        val = find_values(values, temp)
        if val > best:
            best = val
            best_conf = temp
    bounds[key1] = (best, best_conf, time_left)
    bounds[key2] = (best, best_conf, time_left)
    return best_conf


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
    graph = {}
    values = {}
    for line in data:
        spl = line.split(" ")
        ori = spl[1]
        r = int(spl[4].split("=")[1].split(";")[0])
        other = " ".join(spl[9:]).split(", ")
        if ori not in graph.keys():
            graph[ori] = set()
        values[ori] = r
        for oth in other:
            graph[ori].add(oth)
        print(ori, r, other)
    values = {key: value for key, value in values.items() if value > 0}
    print(values)
    ans = find_best(graph, values, set(), 30, "AA", 0)
    print(ans)
    ans = find_values(values, ans)
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
    ans = 0
    graph = {}
    values = {}
    bounds = {}
    for line in data:
        spl = line.split(" ")
        ori = spl[1]
        r = int(spl[4].split("=")[1].split(";")[0])
        other = " ".join(spl[9:]).split(", ")
        if ori not in graph.keys():
            graph[ori] = set()
        values[ori] = r
        for oth in other:
            graph[ori].add(oth)
        print(ori, r, other)
    values = {key: value for key, value in values.items() if value > 0}
    print(values)
    ans = find_best_2(graph, values, set(), 26, ("AA", 0, "AA", 0), 0, bounds)
    print(ans)
    ans = find_values(values, ans)
    return ans


def main():
    day = 16
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    # ans1 = solve1([x for x in data])
    ans2 = solve2([x for x in data])
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
