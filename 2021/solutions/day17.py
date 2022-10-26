from main import *


def solve1(dat):
    data = dat["data"]
    data = data[0].split(" ")
    # print(data)
    x = data[2].split("=")[1].split("..")
    x0, x1 = int(x[0]), int(x[1].strip(","))
    y = data[3].split("=")[1].split("..")
    y0, y1 = int(y[0]), int(y[1].strip(","))
    # print(x0, x1, y0, y1)
    best = -500
    # x=137..171, y=-98..-73
    count = 0
    for vy in range(-100, 1000):
        # tvx = vx
        tvy = vy
        # x = 0
        y = 0
        this_best = y
        while y >= y0:
            # x += tvx
            y += tvy
            this_best = max(this_best, y)
            tvy -= 1
            if y0 <= y <= y1:
                best = max(best, this_best)
                # count += 1
                break
    return best


def solve2(dat):
    data = dat["data"]
    data = data[0].split(" ")
    # print(data)
    x = data[2].split("=")[1].split("..")
    x0, x1 = int(x[0]), int(x[1].strip(","))
    y = data[3].split("=")[1].split("..")
    y0, y1 = int(y[0]), int(y[1].strip(","))
    # print(x0, x1, y0, y1)
    # x=137..171, y=-98..-73
    count = 0
    for vx in range(180):
        for vy in range(-100, 1000):
            tvx = vx
            tvy = vy
            x = 0
            y = 0
            while y >= y0 and x <= x1:
                x += tvx
                y += tvy
                if tvx > 0:
                    tvx -= 1
                elif tvx < 0:
                    tvx += 1
                tvy -= 1
                if x0 <= x <= x1 and y0 <= y <= y1:
                    count += 1
                    break
    return count


def main():
    day = 17
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
