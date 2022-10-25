from main import *


def get(data, x, y, background):
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return "1" if background == "#" else "0"
    return "1" if data[y][x] == "#" else "0"


def enhance(data, decoder, background):
    output = []
    for y in range(-1, len(data) + 1):
        row = []
        for x in range(-1, len(data[0]) + 1):
            binary_string = ""
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    binary_string += get(data, x + dx, y + dy, background)
            row.append(decoder[int(binary_string, 2)])
        output.append("".join(row))
    return output, "#" if background == "." else "."


def solve1(dat):
    data = dat["data"]
    decoder = data[0]
    data = data[1:]
    background = "."
    for i in range(2):
        data, background = enhance(data, decoder, background)
    for row in data:
        pass
        # print(row)
    # print(len(data))
    # print(len(data[0]))
    amount = 0
    for row in data:
        amount += row.count("#")
    return amount


def solve2(dat):
    data = dat["data"]
    decoder = data[0]
    data = data[1:]
    background = "."
    for i in range(50):
        data, background = enhance(data, decoder, background)
    for row in data:
        pass
        # print(row)
    # print(len(data))
    # print(len(data[0]))
    amount = 0
    for row in data:
        amount += row.count("#")
    return amount


def main():
    day = 20
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
