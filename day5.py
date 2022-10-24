from main import *


def solve1(dat):
    data = dat["data"]
    points = [x.split(" -> ") for x in data]
    points = [[[int(z) for z in y.split(",")] for y in x] for x in points]
    max_point = max([max([max(y) for y in x]) for x in points]) + 1
    field = []
    # print(max_point)
    for i in range(max_point + 1):
        row = []
        for i in range(max_point + 1):
            row.append(0)
        field.append(row)
    for point in points:
        start = point[0]
        end = point[1]
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                field[start[0]][i] += 1
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                field[i][start[1]] += 1
    amount = 0
    for row in field:
        for value in row:
            if value >= 2:
                amount += 1
    return amount


def solve2(dat):
    data = dat["data"]
    points = [x.split(" -> ") for x in data]
    points = [[[int(z) for z in y.split(",")] for y in x] for x in points]
    max_point = max([max([max(y) for y in x]) for x in points]) + 1
    field = []
    # print(max_point)
    for i in range(max_point + 1):
        row = []
        for i in range(max_point + 1):
            row.append(0)
        field.append(row)
    for point in points:
        start = point[0]
        end = point[1]
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                field[start[0]][i] += 1
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                field[i][start[1]] += 1
        else:
            x_mod = 1 if end[0] >= start[0] else -1
            y_mod = 1 if end[1] >= start[1] else -1
            size = abs(start[0] - end[0])
            for i in range(size + 1):
                field[start[0] + i * x_mod][start[1] + i * y_mod] += 1

    amount = 0
    for row in field:
        for value in row:
            if value >= 2:
                amount += 1
    return amount


def main():
    day = 5
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
