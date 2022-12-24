from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import random

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

add_const = 100 / 14**5
global depth


def find(oror, clor, obor, obcl, geor, geob, minutes, robots, resources, best_map, key_stack):
    if minutes == 0:
        return resources[3]
    best = 0
    limi = 2
    key = (resources[0], resources[1], resources[2], minutes, robots[0], robots[1], robots[2])
    if key in best_map.keys() and best_map[key] >= resources[3]:
        best_map["o"] += 1
        best_map["d"] += 100 / 5 ** (depth - minutes)
        # print(f"Skipping at {minutes} minutes left and added {100 / (depth - minutes) ** 5}%")
        if best_map["o"] % 100000 == 0:
            print(f"Optimized {best_map['o']} times, with {len(best_map.keys())} keys and {best_map['d']}% done")
        return best_map[key]

    """
    obr_y = robots[2]
    obs_y = resources[2]
    obr_n = robots[2]
    obs_n = resources[2]
    ger_y = 0
    ger_n = 0
    geo_y = 0
    geo_n = 0
    should_build_obs = False
    for i in range(minutes):
        obs_n += obr_n
        obs_y += obr_y
        geo_y += ger_y
        geo_n += ger_n
        if i == 0:
            obr_y += 1
        if obs_n >= geob:
            obs_n -= geob
            ger_n += 1
        if obs_y >= geob:
            obs_y -= geob
            ger_y += 1
        if geo_y > geo_n:
            should_build_obs = True
            break
    """
    should_build_obs = True

    if robots[0] < max(clor, obor, geor):
        if resources[0] >= geor and resources[2] >= geob and minutes > 1:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1], robots[2]), (resources[0] + robots[0] - geor, resources[1] + robots[1], resources[2] + robots[2] - geob, resources[3] + minutes - 1), best_map, key_stack)
            best = max(best, test)
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)

        if resources[0] >= obor and resources[1] >= obcl and minutes > 2 and should_build_obs:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1], robots[2] + 1), (resources[0] + robots[0] - obor, resources[1] + robots[1] - obcl, resources[2] + robots[2], resources[3]), best_map, key_stack)
            best = max(best, test)
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)

        if resources[0] >= clor and minutes > 3:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1] + 1, robots[2]), (resources[0] + robots[0] - clor, resources[1] + robots[1], resources[2] + robots[2], resources[3]), best_map, key_stack)
            best = max(best, test)
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)

        if resources[0] >= oror and minutes > 2:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0] + 1, robots[1], robots[2]), (resources[0] + robots[0] - oror, resources[1] + robots[1], resources[2] + robots[2], resources[3]), best_map, key_stack)
            best = max(best, test)
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)

        test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1], robots[2]), (resources[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3]), best_map, key_stack)
        best = max(best, test)
    else:
        did_robot = False
        if resources[0] >= geor and resources[2] >= geob and minutes > 1:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1], robots[2]), (resources[0] + robots[0] - geor, resources[1] + robots[1], resources[2] + robots[2] - geob, resources[3] + minutes - 1), best_map, key_stack)
            best = max(best, test)
            did_robot = True
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)
        if resources[0] >= obor and resources[1] >= obcl and minutes > 2 and should_build_obs:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1], robots[2] + 1), (resources[0] + robots[0] - obor, resources[1] + robots[1] - obcl, resources[2] + robots[2], resources[3]), best_map, key_stack)
            best = max(best, test)
            did_robot = True
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)
        if resources[0] >= clor and minutes > 3:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1] + 1, robots[2]), (resources[0] + robots[0] - clor, resources[1] + robots[1], resources[2] + robots[2], resources[3]), best_map, key_stack)
            best = max(best, test)
            did_robot = True
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)
        if not did_robot:
            test = find(oror, clor, obor, obcl, geor, geob, minutes - 1, (robots[0], robots[1], robots[2]), (resources[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3]), best_map, key_stack)
            best = max(best, test)
            best_map["d"] -= 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)
        best_map["d"] += 100 / 5 ** (depth - minutes + 1)

    if minutes > limi:
        if key not in best_map.keys():
            while len(key_stack) > 10000000:
                to_rem = random.randint(1, len(key_stack)) - 1
                best_map.pop(key_stack[to_rem])
                key_stack[to_rem] = key_stack[-1]
                key_stack.pop()
            key_stack.append(key)
        best_map[key] = best
    return best



def solve1(data):
    global depth
    depth = 24

    ints = [extract_ints(x) for x in data]
    # first = map_lines(data[:1], [int], ",")
    parsed = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed = my_map(parsed, lambda x: x)

    # SOLUTION
    i = 0
    s = ""
    d = {}
    u = set()
    l = []
    ans = 0
    for line in data:
        pass
    for ini in ints:
        ore_ore = ini[1]
        clay_ore = ini[2]
        obsidian_ore = ini[3]
        obsidian_clay = ini[4]
        geode_ore = ini[5]
        geode_obsidian = ini[6]
        best_map = {"o": 0, "d": 0.0}
        key_stack = []
        data_arr = [depth, 1, 0, 0, 0, 0, 0, 0]  # depth, (ro1, ro2, ro3), (re1, re2, re3, re4)
        temp = find(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian, data_arr, best_map, key_stack)
        ans += temp * ini[0]
        print(f"{ini[0]} done, answer was {temp}")
        # break

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return ans


def solve2(data):
    global depth
    depth = 32
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    ans = 231
    for ini in ints[1:2]:
        ore_ore = ini[1]
        clay_ore = ini[2]
        obsidian_ore = ini[3]
        obsidian_clay = ini[4]
        geode_ore = ini[5]
        geode_obsidian = ini[6]
        best_map = {"o": 0, "d": 0.0}
        key_stack = []
        temp = find(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian, depth, (1, 0, 0), (0, 0, 0, 0), best_map, key_stack)
        ans *= temp
        print(f"{ini[0]} done, answer was {temp}")
    return ans


def main():
    day = 19
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    # ans1 = solve1([x for x in data])
    ans2 = solve2([x for x in data])
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
