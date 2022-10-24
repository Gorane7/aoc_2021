from main import *


def solve1(dat):
    data = dat["data"]
    keep = []
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    matches = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    total = 0
    for line in data:
        scores = {
            "(": 0,
            "[": 0,
            "{": 0,
            "<": 0
        }
        expecting = []
        correct = True
        for chara in line:
            if chara in scores.keys():
                scores[chara] += 1
                expecting.append(chara)
            else:
                matching = matches[chara]
                scores[matching] -= 1
                if expecting[-1] != matching:
                    total += points[chara]
                    correct = False
                    break
                else:
                    expecting = expecting[:-1]
    return total



def solve2(dat):
    data = dat["data"]
    keep = []
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    matches = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    rev_matches = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    scoress = []
    for line in data:
        scores = {
            "(": 0,
            "[": 0,
            "{": 0,
            "<": 0
        }
        expecting = []
        correct = True
        for chara in line:
            if chara in scores.keys():
                scores[chara] += 1
                expecting.append(chara)
            else:
                matching = matches[chara]
                scores[matching] -= 1
                if expecting[-1] != matching:
                    correct = False
                    break
                else:
                    expecting = expecting[:-1]
        if correct:
            score = 0
            for chara in expecting[::-1]:
                score *= 5
                score += points[rev_matches[chara]]
            scoress.append(score)
    return sorted(scoress)[len(scoress) // 2]


def main():
    day = 10
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
