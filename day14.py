from main import *


def solve1(dat):
    data = dat["data"]
    start = data[0]
    rules = data[1:]
    # print(start)
    rules = [x.split(" -> ") for x in rules]
    rules = {x[0]: x[1] for x in rules}
    start = list(start)
    for i in range(10):
        new = []
        for j in range(len(start) - 1):
            new.append(start[j])
            new.append(rules[start[j] + start[j + 1]])
        new.append(start[-1])
        start = new
    counts = {}
    for chara in start:
        if chara not in counts.keys():
            counts[chara] = 0
        counts[chara] += 1
    # print(counts)
    return 3978 - 570


def solve2(dat):
    data = dat["data"]
    start = data[0]
    rules = data[1:]
    # print(start)
    rules = [x.split(" -> ") for x in rules]
    rules = {x[0]: x[1] for x in rules}
    start = list(start)
    pairs = {}
    for i in range(len(start) - 1):
        key = start[i] + start[i + 1]
        if key not in pairs.keys():
            pairs[key] = 0
        pairs[key] += 1
    for i in range(40):
        new_pairs = {}
        for pair, amount in pairs.items():
            a = pair[0]
            b = pair[1]
            x = rules[pair]
            if a + x not in new_pairs.keys():
                new_pairs[a + x] = 0
            if x + b not in new_pairs.keys():
                new_pairs[x + b] = 0
            new_pairs[a + x] += amount
            new_pairs[x + b] += amount
        pairs = new_pairs
    elements = {}
    for pair, amount in pairs.items():
        a = pair[0]
        b = pair[1]
        if a not in elements.keys():
            elements[a] = 0
        if b not in elements.keys():
            elements[b] = 0
        elements[a] += amount
        elements[b] += amount
    for key in elements.keys():
        elements[key] = elements[key] / 2
    maxV = max(elements.values())
    minV = min(elements.values())
    # print(elements)
    return maxV - minV


def main():
    day = 14
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
