import random

from main import *


def solve1(dat):
    data = dat["data"]
    data = [x.split(" | ") for x in data]
    data = [[y.split(" ") for y in x] for x in data]
    amount = 0
    for row in data:
        for item in row[1]:
            if len(item) in [2, 4, 3, 7]:
                amount += 1
    return amount


def solve2(dat):
    data = dat["data"]
    data = [x.split(" | ") for x in data]
    data = [[y.split(" ") for y in x] for x in data]
    amount = 0
    for row in data:
        # print(row[0])
        decoding = decode(row[0])
        # print(decoding)
        amount += calculate(decoding, row[1])
    return amount


def decode(row):
    decoding = {}
    possibility_map = {}
    letters = "abcdefg"
    for letter in letters:
        possibility_map[letter] = [chara for chara in letters]
    row = sorted(row, key=lambda x: len(x))
    mapping = generate_random()
    while not solves(mapping, row):
        mapping = generate_random()
    # print(mapping)
    return make_decoding(mapping, row)


def make_decoding(mapping, row):
    numbers = {
        "abcefg": 0,
        "abdefg": 6,
        "abcdfg": 9,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "abdfg": 5,
        "bcdf": 4,
        "acf": 7,
        "abcdefg": 8
    }
    answer = {}
    for item in row:
        answer["".join(sorted([chara for chara in item]))] = numbers["".join(sorted([mapping[x] for x in item]))]
    return answer


def solves(mapping, row):
    numbers = {
        "abcefg": 0,
        "abdefg": 6,
        "abcdfg": 9,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "abdfg": 5,
        "bcdf": 4,
        "acf": 7,
        "abcdefg": 8
    }
    for item in row:
        this = ""
        for chara in item:
            this += mapping[chara]
        solved = False
        for key, value in numbers.items():
            if sorted(this) == sorted(key):
                solved = True
                break
        if not solved:
            return False
    return True


def generate_random():
    letters = "abcdefg"
    mapping = {}
    for letter in letters:
        choice = random.choice(letters)
        while choice in mapping.values():
            choice = random.choice(letters)
        mapping[letter] = choice
    return mapping


def calculate(decoding, row):
    mults = [1000, 100, 10, 1]
    total = 0
    for i, item in enumerate(row):
        total += decoding["".join(sorted(item))] * mults[i]
    return total


def main():
    day = 8
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
