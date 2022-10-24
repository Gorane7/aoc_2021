from main import *


def solve1(dat):
    data = dat["data"]
    best = -500
    # x=137..171, y=-98..-73
    count = 0
    for vx in range(180):
        for vy in range(-100, 1000):
            tvx = vx
            tvy = vy
            x = 0
            y = 0
            this_best = y
            while y >= -98 and x <= 171:
                x += tvx
                y += tvy
                this_best = max(this_best, y)
                if tvx > 0:
                    tvx -= 1
                elif tvx < 0:
                    tvx += 1
                tvy -= 1
                if 137 <= x <= 171 and -98 <= y <= -73:
                    best = max(best, this_best)
                    count += 1
                    break
    return count


def solve2(dat):
    data = dat["data"]


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
