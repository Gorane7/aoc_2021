import sys
sys.setrecursionlimit(2000)
import random

from main import *

HALLWAYS = [2, 4, 6, 8]
NAMES = {"A": 0,
         "B": 1,
         "C": 2,
         "D": 3
         }
COSTS = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}
BEST_SOL = 46000
SOLUTIONS = 0

def solve1(dat):
    data = dat["data"]
    hallway = [None] * 11
    up = ["D", "D", "B", "A"]
    down = ["C", "A", "B", "C"]
    cost = solve(hallway, up, down, 0, 0)


def should_move_to_room(i, hallway, up, down):
    if down[NAMES[hallway[i]]] is not None and down[NAMES[hallway[i]]] != hallway[i]:
        return 0, -1
    if up[NAMES[hallway[i]]] is not None and up[NAMES[hallway[i]]] != hallway[i]:
        return 0, -1
    target = HALLWAYS[NAMES[hallway[i]]]
    n = i
    steps_taken = 0
    while n != target:
        steps_taken += 1
        if n > target:
            n -= 1
            if hallway[n] is not None:
                return 0, -1
        else:
            n += 1
            if hallway[n] is not None:
                return 0, -1
    if down[NAMES[hallway[i]]] is None:
        return 2, steps_taken + 2
    return 1, steps_taken + 1


def should_move_to_room2(i, hallway, caves):
    # print(f"Cchecking for {i}, animal is {hallway[i]}")
    for j in range(len(caves)):
        # print(f"Pre checking {j}")
        current = caves[j][NAMES[hallway[i]]]
        if current is not None and current != hallway[i]:
            return 0, -1
    # print(f"Got past {caves}")
    target = HALLWAYS[NAMES[hallway[i]]]
    n = i
    steps_taken = 0
    while n != target:
        steps_taken += 1
        if n > target:
            n -= 1
            if hallway[n] is not None:
                return 0, -1
        else:
            n += 1
            if hallway[n] is not None:
                return 0, -1
    for j in range(len(caves) - 1, -1, -1):
        # print(f"Checking: {j}")
        if caves[j][NAMES[hallway[i]]] is None:
            return j + 1, steps_taken + j + 1
    # print("PROBLEMS 111")


def has_free_path(hallway, start, end):
    i = start
    while i != end:
        if i < end:
            i += 1
        else:
            i -= 1
        if hallway[i] is not None:
            return False
    return True


def pretty_print(hallway, up, down, level):
    pass
    # print(f"Level: {level}")
    # print("".join([("." if x is None else x) for x in hallway]))
    # print(f"##{'#'.join([('.' if x is None else x) for x in up])}##")
    # print(f"##{'#'.join([('.' if x is None else x) for x in down])}##")
    # print()


def solve(hallway, up, down, cost, level):
    global BEST_SOL
    global SOLUTIONS
    # pretty_print(hallway, up, down, level)
    if cost >= BEST_SOL:
        SOLUTIONS += 1
        if SOLUTIONS % 1000000 == 0:
            print(f"Have found {SOLUTIONS // 1000000}M solutions")
        return cost
    if up == ["A", "B", "C", "D"] and down == ["A", "B", "C", "D"]:
        SOLUTIONS += 1
        if SOLUTIONS % 1000000 == 0:
            print(f"Have found {SOLUTIONS // 1000000}M solutions")
        return cost

    # Move into room
    moves_to_room = [(i, el) for i, el in enumerate(hallway) if el is not None]
    random.shuffle(moves_to_room)
    for i, el in moves_to_room:
        move_to_room, steps = should_move_to_room(i, hallway, up, down)
        if move_to_room:
            if move_to_room == 1:
                up[NAMES[hallway[i]]] = el
                hallway[i] = None
                this_sol = solve(hallway, up, down, cost + steps * COSTS[el], level + 1)
                if this_sol < BEST_SOL:
                    BEST_SOL = this_sol
                    print(f"Found new and better solution: {BEST_SOL}")
                hallway[i] = el
                up[NAMES[hallway[i]]] = None
            else:
                down[NAMES[hallway[i]]] = el
                hallway[i] = None
                this_sol = solve(hallway, up, down, cost + steps * COSTS[el], level + 1)
                if this_sol < BEST_SOL:
                    BEST_SOL = this_sol
                    print(f"Found new and better solution: {BEST_SOL}")
                hallway[i] = el
                down[NAMES[hallway[i]]] = None

    # Move out of room
    target_rooms = [i for i in range(4)]
    random.shuffle(target_rooms)
    for i in target_rooms:
        if up[i] is not None:
            if NAMES[up[i]] == i:
                continue
            j = HALLWAYS[i]
            for times in [-1, 1]:
                if times == -1:
                    js = [x for x in range(j)]
                else:
                    js = [x for x in range(j + 1, 11)]
                random.shuffle(js)
                for tj in js:
                    # tj = j + times * dj
                    if tj in HALLWAYS:
                        continue
                    if not has_free_path(hallway, HALLWAYS[i], tj):
                        break
                    steps = abs(tj - HALLWAYS[i]) + 1
                    el = up[i]
                    hallway[tj] = el
                    up[i] = None
                    this_sol = solve(hallway, up, down, cost + steps * COSTS[el], level + 1)
                    if this_sol < BEST_SOL:
                        BEST_SOL = this_sol
                        # print(f"Found new and better solution: {BEST_SOL}")
                    up[i] = el
                    hallway[tj] = None
        elif down[i] is not None:
            if NAMES[down[i]] == i:
                continue
            j = HALLWAYS[i]
            for times in [-1, 1]:
                if times == -1:
                    js = [x for x in range(j)]
                else:
                    js = [x for x in range(j + 1, 11)]
                random.shuffle(js)
                for tj in js:
                    # tj = j + times * dj
                    if tj in HALLWAYS:
                        continue
                    if not has_free_path(hallway, HALLWAYS[i], tj):
                        break
                    steps = abs(tj - HALLWAYS[i]) + 2
                    el = down[i]
                    hallway[tj] = el
                    down[i] = None
                    this_sol = solve(hallway, up, down, cost + steps * COSTS[el], level + 1)
                    if this_sol < BEST_SOL:
                        BEST_SOL = this_sol
                        # print(f"Found new and better solution: {BEST_SOL}")
                    down[i] = el
                    hallway[tj] = None

    return BEST_SOL


def solve_for_2(hallway, caves, cost, level, moves):
    global BEST_SOL
    global SOLUTIONS
    # pretty_print(hallway, up, down, level)
    if cost >= BEST_SOL:
        SOLUTIONS += 1
        if SOLUTIONS % 1000000 == 0:
            pass
            # print(f"Have found {SOLUTIONS // 1000000}M solutions")
        return cost
    all_match = True
    for i in range(len(caves)):
        if caves[i] != ["A", "B", "C", "D"]:
            all_match = False
            break
    if all_match:
        SOLUTIONS += 1
        if SOLUTIONS % 1000000 == 0:
            pass
            # print(f"Have found {SOLUTIONS // 1000000}M solutions")
        return cost

    # Move into room
    moves_to_room = [(i, el) for i, el in enumerate(hallway) if el is not None]
    random.shuffle(moves_to_room)
    for i, el in moves_to_room:
        move_to_room, steps = should_move_to_room2(i, hallway, caves)
        if move_to_room:
            caves[move_to_room - 1][NAMES[hallway[i]]] = el
            hallway[i] = None
            moves.append(f"H{i}{el}->R{move_to_room}")
            this_sol = solve_for_2(hallway, caves, cost + steps * COSTS[el], level + 1, moves)
            moves.pop()
            if this_sol < BEST_SOL:
                BEST_SOL = this_sol
                # print(f"Found new and better solution: {BEST_SOL} ... {', '.join(moves)}")
            hallway[i] = el
            caves[move_to_room - 1][NAMES[hallway[i]]] = None

    # Move out of room
    target_rooms = [i for i in range(4)]
    random.shuffle(target_rooms)
    for i in target_rooms:
        contains_foreign = False
        for j in range(len(caves)):
            if caves[j][i] is not None and NAMES[caves[j][i]] != i:
                contains_foreign = True
        if not contains_foreign:
            continue
        cave_level = -1
        for j in range(len(caves)):
            if caves[j][i] is not None:
                cave_level = j
                break
        j = HALLWAYS[i]
        for times in [-1, 1]:
            if times == -1:
                js = [x for x in range(j)]
            else:
                js = [x for x in range(j + 1, 11)]
            random.shuffle(js)
            for tj in js:
                # tj = j + times * dj
                if tj in HALLWAYS:
                    continue
                if not has_free_path(hallway, HALLWAYS[i], tj):
                    continue
                steps = abs(tj - HALLWAYS[i]) + cave_level + 1
                el = caves[cave_level][i]
                hallway[tj] = el
                caves[cave_level][i] = None
                moves.append(f"R{i} {cave_level}{el}->H{tj}")
                this_sol = solve_for_2(hallway, caves, cost + steps * COSTS[el], level + 1, moves)
                moves.pop()
                if this_sol < BEST_SOL:
                    BEST_SOL = this_sol
                    # print(f"Found new and better solution: {BEST_SOL} ... {', '.join(moves)}")
                caves[cave_level][i] = el
                hallway[tj] = None
    return BEST_SOL


def solve2(dat):
    data = dat["data"]
    hallway = [None] * 11
    up = ["D", "D", "B", "A"]
    down = ["C", "A", "B", "C"]
    caves = [
        ["D", "D", "B", "A"],
        ["D", "C", "B", "A"],
        ["D", "B", "A", "C"],
        ["C", "A", "B", "C"]
    ]
    cost = solve_for_2(hallway, caves, 0, 0, [])


def main():
    day = 23
    basic = [("...", "{string}")]
    ints = [("...", "{int}")]
    input_format = basic
    data = parse_input(day, input_format)
    if data["data"]:
        print("Got data successfully")
    else:
        print("Error getting data")
    # ans1 = solve1(data)
    ans1 = "Skipping"
    ans2 = solve2(data)
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
