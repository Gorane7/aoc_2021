import time

from main import *


def solve1(dat):
    data = dat["data"]
    var_locs = {
        "w": 0,
        "x": 1,
        "y": 2,
        "z": 3
    }
    var = [0, 0, 0, 0]
    possible_numbers = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
    hypo_input = [0] * 14
    input_counter = 0
    counter = 0
    commands = [line.split(" ") for line in data]
    for command in commands:
        if command[0] == "inp":
            command[0] = 0
        elif command[0] == "add":
            command[0] = 1
        elif command[0] == "mul":
            command[0] = 2
        elif command[0] == "div":
            command[0] = 3
        elif command[0] == "mod":
            command[0] = 4
        elif command[0] == "eql":
            command[0] = 5
        if command[1] not in "wxyz":
            command[1] = int(command[1])
        if command[1] not in var_locs.keys():
            var_locs[command[1]] = len(var)
            var.append(command[1])
        command[1] = var_locs[command[1]]
        if len(command) > 2:
            if command[2] not in "wxyz":
                command[2] = int(command[2])
            if command[2] not in var_locs.keys():
                var_locs[command[2]] = len(var)
                var.append(command[2])
            command[2] = var_locs[command[2]]
    start = time.time()
    while True:
        counter += 1
        for sp in commands:
            if sp[0] == 0:
                var[sp[1]] = int(possible_numbers[hypo_input[input_counter]])
                input_counter += 1
            elif sp[0] == 1:
                var[sp[1]] = var[sp[1]] + var[sp[2]]
            elif sp[0] == 2:
                var[sp[1]] = var[sp[1]] * var[sp[2]]
            elif sp[0] == 3:
                if var[sp[1]] < 0:
                    var[sp[1]] = - (-var[sp[1]]) // var[sp[2]]
                else:
                    var[sp[1]] = var[sp[1]] // var[sp[2]]
            elif sp[0] == 4:
                var[sp[1]] = var[sp[1]] % var[sp[2]]
            elif sp[0] == 5:
                var[sp[1]] = 1 if var[sp[1]] == var[sp[2]] else 0
        if var[3] == 0:
            # print(f"{''.join([possible_numbers[x] for x in hypo_input])} -> {var[3]}")
            exit()
        if counter % 100000 == 0:
            pass
            # print(hypo_input)
            # print(f"{''.join([possible_numbers[x] for x in hypo_input])} -> {var[3]}")
            # print(f"{counter / (time.time() - start)} checks per second")
            # print()
        # 99999999997338 -> 4878041437
        for i in range(13, -1, -1):
            hypo_input[i] += 1
            if hypo_input[i] > 8:
                hypo_input[i] = 0
            else:
                break
        var[0] = 0
        var[1] = 0
        var[2] = 0
        var[3] = 0
        input_counter = 0
    return var



def solve2(dat):
    data = dat["data"]


def main():
    day = 24
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
