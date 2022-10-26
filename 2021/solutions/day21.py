from main import *


def roll(amount_rolled, next_die):
    amount_rolled += next_die
    next_die += 1
    if next_die > 100:
        next_die = 1
    return amount_rolled, next_die


def solve1(dat):
    data = dat["data"]
    pos1 = 0
    pos2 = 5
    score1 = 0
    score2 = 0
    next_die = 1
    times_rolled = 0
    turn1 = True
    while score1 < 1000 and score2 < 1000:
        times_rolled += 3
        amount_rolled = 0
        for i in range(3):
            amount_rolled, next_die = roll(amount_rolled, next_die)
        if turn1:
            pos1 = (pos1 + amount_rolled) % 10
            score1 += pos1 + 1
        else:
            pos2 = (pos2 + amount_rolled) % 10
            score2 += pos2 + 1
        turn1 = not turn1
    if score1 >= 1000:
        return score2 * times_rolled
    return score1 * times_rolled


def solve2(dat):
    data = dat["data"]
    # pos1, score1, pos2, score2
    data = []
    for i in range(10):
        row = []
        for j in range(21):
            roww = []
            for k in range(10):
                rowww = []
                for l in range(21):
                    rowww.append(0)
                roww.append(rowww)
            row.append(roww)
        data.append(row)
    data[0][0][5][0] = 1
    turn1 = True
    times_won1 = 0
    times_won2 = 0
    while True:
        new = []
        for i in range(10):
            row = []
            for j in range(21):
                roww = []
                for k in range(10):
                    rowww = []
                    for l in range(21):
                        rowww.append(0)
                    roww.append(rowww)
                row.append(roww)
            new.append(row)
        changed = False
        for pos1, row in enumerate(data):
            for score1, roww in enumerate(row):
                for pos2, rowww in enumerate(roww):
                    for score2, amount in enumerate(rowww):
                        if amount == 0:
                            continue
                        for delta1 in range(1, 4):
                            for delta2 in range(1, 4):
                                for delta3 in range(1, 4):
                                    delta = delta1 + delta2 + delta3
                                    new_pos1 = pos1
                                    new_pos2 = pos2
                                    new_score1 = score1
                                    new_score2 = score2
                                    if turn1:
                                        new_pos1 = (new_pos1 + delta) % 10
                                        new_score1 = new_score1 + new_pos1 + 1
                                    else:
                                        new_pos2 = (new_pos2 + delta) % 10
                                        new_score2 = new_score2 + new_pos2 + 1
                                    if new_score1 >= 21:
                                        times_won1 += amount
                                        continue
                                    if new_score2 >= 21:
                                        times_won2 += amount
                                        continue
                                    changed = True
                                    new[new_pos1][new_score1][new_pos2][new_score2] += amount
        data = new
        turn1 = not turn1
        if not changed:
            break
    return max(times_won1, times_won2)


def main():
    day = 21
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
