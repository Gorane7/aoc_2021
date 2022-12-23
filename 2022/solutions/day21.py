from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def solve1(data):

    # ints = [extract_ints(x) for x in data]
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
    for line in data:
        a, b = line.split(": ")
        if b.isnumeric():
            graph[a] = int(b)
        else:
            graph[a] = b.split(" ")
    while not isinstance(graph["root"], int):
        for name, value in graph.items():
            if isinstance(value, int):
                continue
            if isinstance(graph[value[0]], int) and isinstance(graph[value[2]], int):
                if value[1] == "-":
                    graph[name] = graph[value[0]] - graph[value[2]]
                if value[1] == "+":
                    graph[name] = graph[value[0]] + graph[value[2]]
                if value[1] == "*":
                    graph[name] = graph[value[0]] * graph[value[2]]
                if value[1] == "/":
                    graph[name] = graph[value[0]] // graph[value[2]]
    ans = graph["root"]

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return ans


def find_path(graph, target):
    if target == "humn":
        return "humn"
    if isinstance(graph[target], int):
        return graph[target]
    temp = [find_path(graph, graph[target][0]), graph[target][1], find_path(graph, graph[target][2])]
    if isinstance(temp[0], int) and isinstance(temp[2], int):
        if temp[1] == "-":
            return temp[0] - temp[2]
        if temp[1] == "+":
            return temp[0] + temp[2]
        if temp[1] == "*":
            return temp[0] * temp[2]
        if temp[1] == "/":
            return temp[0] // temp[2]
    return temp


def calc(temp, humn_val):
    if isinstance(temp, int):
        return temp
    if isinstance(temp, str):
        return humn_val
    if temp[1] == "-":
        return calc(temp[0], humn_val) - calc(temp[2], humn_val)
    if temp[1] == "+":
        return calc(temp[0], humn_val) + calc(temp[2], humn_val)
    if temp[1] == "*":
        return calc(temp[0], humn_val) * calc(temp[2], humn_val)
    if temp[1] == "/":
        return calc(temp[0], humn_val) // calc(temp[2], humn_val)


def must_equal(equation, value):
    if isinstance(equation, str):
        return value
    if isinstance(equation[0], int):
        if equation[1] == "+":
            return must_equal(equation[2], value - equation[0])
        if equation[1] == "-":
            return must_equal(equation[2], equation[0] - value)
        if equation[1] == "*":
            t = value // equation[0]
            if t * equation[0] != value:
                return 0
            return must_equal(equation[2], t)
        if equation[1] == "/":
            b = equation[0] // value
            possible_values = []
            d = 0
            while equation // (b + d) == c or equation // (b - d) == c:
                if equation // (b + d) == c:
                    if b + d not in possible_values:
                        possible_values.append(b + d)
                if equation // (b - d) == c:
                    if b - d not in possible_values:
                        possible_values.append(b - d)
            for value in possible_values:
                t = must_equal(equation[2], value)
                if t != 0:
                    return t
            return 0
    if isinstance(equation[2], int):
        if equation[1] == "+":
            return must_equal(equation[0], value - equation[2])
        if equation[1] == "-":
            return must_equal(equation[0], equation[2] + value)
        if equation[1] == "*":
            t = value // equation[2]
            if t * equation[2] != value:
                return 0
            return must_equal(equation[0], t)
        if equation[1] == "/":
            possible_values = []
            for i in range(equation[2]):
                possible_values.append(value * equation[2] + i)
            for value in possible_values:
                t = must_equal(equation[0], value)
                if t != 0:
                    return t
            return 0



def solve2(data):
    graph = {}
    for line in data:
        a, b = line.split(": ")
        if b.isnumeric():
            graph[a] = int(b)
        else:
            graph[a] = b.split(" ")
    graph["humn"] = "humn"
    path = find_path(graph, "root")
    return must_equal(path[0], path[2])


def main():
    day = 21
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
