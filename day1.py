from main import *


def solve1(data):
    dat = data["data"]
    parse1 = []
    prev = None
    counter = 0
    for i, line in enumerate(dat):
        if prev is None:
            prev = line
            continue
        if line > prev:
            counter += 1
        prev = line
    return counter


def solve2(data):
    dat = data["data"]
    parse1 = []
    prev = []
    counter = 0
    for i, line in enumerate(dat):
        if len(prev) < 3:
            prev.append(line)
            continue
        pre = sum(prev)
        prev.pop(0)
        prev.append(line)
        post = sum(prev)
        if post > pre:
            counter += 1
    return counter


def main():
    basic = [("...", "{string}")]
    ints = [("...", "{int}")]
    input_format = ints
    data = parse_input(1, input_format)
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
