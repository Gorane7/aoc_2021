from main import *


def solve1(data):
    dat = data["data"]
    one_amount = [0] * len(dat[0])
    zero_amount = [0] * len(dat[0])
    for word in dat:
        for i, letter in enumerate(word):
            if letter == "1":
                one_amount[i] += 1
            else:
                zero_amount[i] += 1
    total = []
    for i in range(len(one_amount)):
        if one_amount[i] > zero_amount[i]:
            total.append("1")
        else:
            total.append("0")
    total = total[::-1]
    ans1 = 0
    ans2 = 0
    mult = 1
    for let in total:
        ans1 += mult * int(let)
        ans2 += mult * (0 if let == "1" else 1)
        mult = mult * 2
    return ans1 * ans2


def solve2(data):
    dat = data["data"]
    one_amount = [0] * len(dat[0])
    zero_amount = [0] * len(dat[0])
    for word in dat:
        for i, letter in enumerate(word):
            if letter == "1":
                one_amount[i] += 1
            else:
                zero_amount[i] += 1
    # print(one_amount)
    # print(zero_amount)
    most = [(i, x) for i, x in enumerate(dat)]
    least = [(i, x) for i, x in enumerate(dat)]
    while len(most) > 1:
        ones = len([x for x in most if x[1][0] == "1"])
        zeros = len(most) - ones
        if ones >= zeros:
            most = [(x[0], x[1][1:]) for x in most if x[1][0] == "1"]
        else:
            most = [(x[0], x[1][1:]) for x in most if x[1][0] == "0"]
        # print(most)
    while len(least) > 1:
        ones = len([x for x in least if x[1][0] == "1"])
        zeros = len(least) - ones
        if ones >= zeros:
            least = [(x[0], x[1][1:]) for x in least if x[1][0] == "0"]
        else:
            least = [(x[0], x[1][1:]) for x in least if x[1][0] == "1"]
        # print(least)
    ans1 = dat[831][::-1]
    ans2 = dat[856][::-1]
    mult = 1
    ans1d = 0
    ans2d = 0
    for first, second in zip(ans1, ans2):
        ans1d += mult * int(first)
        ans2d += mult * int(second)
        mult = mult * 2
    # print(ans1)
    # print(ans2)
    return ans1d * ans2d


def main():
    day = 3
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
