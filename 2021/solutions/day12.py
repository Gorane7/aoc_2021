from main import *


def solve1(dat):
    data = dat["data"]
    data = [x.split("-") for x in data]
    graph = {}
    for a in data:
        if a[0] not in graph.keys():
            graph[a[0]] = []
        if a[1] not in graph.keys():
            graph[a[1]] = []
        graph[a[0]].append(a[1])
        graph[a[1]].append(a[0])
    paths = set()
    stack = []
    stack.append((["start"], {"start"}))
    while stack:
        el = stack.pop()
        for next_el in graph[el[0][-1]]:
            is_large = next_el.isupper()
            if not is_large and next_el in el[1]:
                continue
            if next_el == "end":
                paths.add("-".join(el[0]))
                continue
            stack.append(([x for x in el[0]] + [next_el], el[1].union({next_el}) if not is_large else {x for x in el[1]}))
    return len(paths)


def solve2(dat):
    data = dat["data"]
    data = [x.split("-") for x in data]
    graph = {}
    for a in data:
        if a[0] not in graph.keys():
            graph[a[0]] = []
        if a[1] not in graph.keys():
            graph[a[1]] = []
        graph[a[0]].append(a[1])
        graph[a[1]].append(a[0])
    paths = set()
    stack = []
    stack.append((["start"], {"start"}, None))
    while stack:
        el = stack.pop()
        for next_el in graph[el[0][-1]]:
            is_large = next_el.isupper()
            if next_el == "end":
                paths.add("-".join(el[0]))
                continue
            if not is_large and next_el in el[1]:
                if el[2] is None and next_el != "start":
                    stack.append(([x for x in el[0]] + [next_el], {x for x in el[1]}, next_el))
                continue
            stack.append(([x for x in el[0]] + [next_el], el[1].union({next_el}) if not is_large else {x for x in el[1]}, el[2]))
    return len(paths)


def main():
    day = 12
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
