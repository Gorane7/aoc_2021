from main import *

import random


def rotate(x, y, times):
    if times == 0:
        return x, y
    return rotate(y, - x, times - 1)


def find_rotations(data, combinations=None):
    return_data = []
    counter = -1
    was_none = False
    if combinations is None:
        was_none = True
        combinations = []
    while len(return_data) < 24:
        counter += 1
        if was_none:
            x_rot = random.randint(0, 3)
            y_rot = random.randint(0, 3)
            z_rot = random.randint(0, 3)
        else:
            x_rot, y_rot, z_rot = combinations[counter][0], combinations[counter][1], combinations[counter][2]
        this_rot = set()

        for el in data:
            elc = el[:]
            elc[1], elc[2] = rotate(elc[1], elc[2], x_rot)
            elc[0], elc[2] = rotate(elc[0], elc[2], y_rot)
            elc[0], elc[1] = rotate(elc[0], elc[1], z_rot)
            this_rot.add((elc[0], elc[1], elc[2]))
        if this_rot in return_data:
            # print(f"Iteration {counter}, found duplicate")
            continue
        # print(f"Iteration {counter}, found match")
        if was_none:
            if x_rot >= 2 and y_rot >= 2 and z_rot >= 2:
                combinations.append((x_rot - 2, y_rot - 2, z_rot - 2))
            else:
                combinations.append((x_rot, y_rot, z_rot))
        return_data.append([x for x in this_rot])
    # print(sorted(combinations))
    return return_data, combinations



def find_rotations_old(data):
    return_data = []
    for i in range(24):
        this = []
        direction = i // 4
        rotation = i % 4
        for el in data:
            el_copy = el[:]
            if direction in [0, 1]:
                if direction == 0:
                    pass
                elif direction == 1:
                    el_copy[1], el_copy[2] = rotate(el_copy[1], el_copy[2], 2)
                el_copy[1], el_copy[2] = rotate(el_copy[1], el_copy[2], rotation)
            elif direction in [2, 3]:
                if direction == 2:
                    el_copy[0], el_copy[1] = rotate(el_copy[0], el_copy[1], 1)
                elif direction == 3:
                    el_copy[0], el_copy[1] = rotate(el_copy[0], el_copy[1], 3)
                el_copy[1], el_copy[2] = rotate(el_copy[1], el_copy[2], rotation)
            elif direction in [4, 5]:
                if direction == 4:
                    el_copy[0], el_copy[2] = rotate(el_copy[0], el_copy[2], 1)
                elif direction == 5:
                    el_copy[0], el_copy[2] = rotate(el_copy[0], el_copy[2], 1)
                el_copy[1], el_copy[2] = rotate(el_copy[1], el_copy[2], rotation)
        return_data.append(this)
    return return_data


def validate(x):
    sets = [set(y) for y in x]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if sets[i] == sets[j]:
                return False
    return True


def generate_relative_locs(amount):
    matrix = []
    for i in range(amount):
        row = []
        for j in range(amount):
            if i == j:
                row.append((0, 0, 0, 0))
            else:
                row.append(None)
        matrix.append(row)
    return matrix


def find_match_amount(list1, list2, ds):
    match_amount = 0
    i = 0
    j = -1
    while True:
        j += 1
        if j >= len(list2):
            i += 1
            j = 0
            if i >= len(list1):
                break
        if list1[i][0] + ds[0] == list2[j][0] and list1[i][1] + ds[1] == list2[j][1] and list1[i][2] + ds[2] == list2[j][2]:
            match_amount += 1
            list1.pop(i)
            list2.pop(j)
            i = 0
            j = -1
    return match_amount


def try_to_match(data1, data2):
    orientation1 = data1[0]
    for o, orientation2 in enumerate(data2):
        # print(f"Comparing {orientation1} with {orientation2}")
        # init_beacon_1 = orientation1[0]
        # init_beacon_2 = orientation2[0]
        # ds = (init_beacon_2[0] - init_beacon_1[0], init_beacon_2[1] - init_beacon_1[1], init_beacon_2[2] - init_beacon_1[2])
        for i in range(len(orientation1)):
            for j in range(len(orientation2)):
                beacon_1 = orientation1[i]
                beacon_2 = orientation2[j]
                ds = (beacon_2[0] - beacon_1[0], beacon_2[1] - beacon_1[1], beacon_2[2] - beacon_1[2])
                matches = find_match_amount(orientation1[:], orientation2[:], ds)
                if matches >= 12:
                    return o, ds[0], ds[1], ds[2]
                # print(f"Comparing {beacon1} with {beacon2}")


def deduce(rel_locations):
    changes = False
    for i in range(len(rel_locations)):
        for j in range(len(rel_locations)):
            pass


def full(rel_locations):
    missing = 0
    for row in rel_locations:
        for el in row:
            if el is None:
                missing += 1
    # print(f"Still missing: {missing}")
    return missing == 0


def add(beacon_data, beacons, deltas):
    for i, row in enumerate(beacon_data):
        # print(f"{100 * i / len(beacon_data)}% done")
        for x_rot in range(4):
            for y_rot in range(4):
                for z_rot in range(4):
                    for existing in beacons:
                        elc = [existing[0], existing[1], existing[2]]
                        elc[1], elc[2] = rotate(elc[1], elc[2], x_rot)
                        elc[0], elc[2] = rotate(elc[0], elc[2], y_rot)
                        elc[0], elc[1] = rotate(elc[0], elc[1], z_rot)
                        for new_i in range(len(row)):
                            new = row[new_i]
                            ds = (new[0] - elc[0], new[1] - elc[1], new[2] - elc[2])
                            matches = 0
                            for trial_i in range(len(row)):
                                trial = row[trial_i][:]
                                trial[0] -= ds[0]
                                trial[1] -= ds[1]
                                trial[2] -= ds[2]
                                trial[0], trial[1] = rotate(trial[0], trial[1], 4 - z_rot)
                                trial[0], trial[2] = rotate(trial[0], trial[2], 4 - y_rot)
                                trial[1], trial[2] = rotate(trial[1], trial[2], 4 - x_rot)
                                if (trial[0], trial[1], trial[2]) in beacons:
                                    matches += 1
                            if matches >= 12:
                                dss = [ds[0], ds[1], ds[2]]
                                dss[0], dss[1] = rotate(dss[0], dss[1], 4 - z_rot)
                                dss[0], dss[2] = rotate(dss[0], dss[2], 4 - y_rot)
                                dss[1], dss[2] = rotate(dss[1], dss[2], 4 - x_rot)
                                deltas.append(dss)
                                # print(f"Found {matches} matches, have {len(beacon_data) - 1} beacons remaining")
                                for trial_i in range(len(row)):
                                    trial = row[trial_i][:]
                                    trial[0] -= ds[0]
                                    trial[1] -= ds[1]
                                    trial[2] -= ds[2]
                                    trial[0], trial[1] = rotate(trial[0], trial[1], 4 - z_rot)
                                    trial[0], trial[2] = rotate(trial[0], trial[2], 4 - y_rot)
                                    trial[1], trial[2] = rotate(trial[1], trial[2], 4 - x_rot)
                                    if (trial[0], trial[1], trial[2]) not in beacons:
                                        beacons.add((trial[0], trial[1], trial[2]))
                                beacon_data.pop(i)
                                return


def solve1(dat):
    data = dat["data"]
    beacon_data = []
    this_beacon = []
    counter = 0
    for line in data:
        if line[:3] == "---":
            if len(this_beacon) > 0:
                beacon_data.append(this_beacon)
                this_beacon = []
        else:
            this_beacon.append([int(x) for x in line.split(",")])
    beacon_data.append(this_beacon)
    beacons = set()
    base_beacon = beacon_data[0]
    beacon_data = beacon_data[1:]
    for beacon in base_beacon:
        beacons.add((beacon[0], beacon[1], beacon[2]))
    scanners = [(0, 0, 0), (54, 1205, -34), (-1129, 1313, 51), (2471, -81, 53), (-3691, -46, 64), (63, -96, -4931),
                (-4793, -1156, -50), (1255, 13, 4801), (-1162, -3686, 1163), (1209, -4812, -1183), (1208, 1217, 3707),
                (-6106, 1274, 1316), (-18, -99, -6093), (-1187, -82, 6059), (2451, 106, -6008), (-4924, 1089, 2450),
                (7241, 2345, 24), (-2335, 8511, -49), (3554, 18, -1089), (1229, -4908, -1131), (-79, 1213, -3580),
                (-36, -5975, 1202), (115, 6016, 2431), (6107, -3677, -47), (77, -1202, 7326), (40, -5990, -1167),
                (1267, -4757, 2436), (-2459, -3739, -1242), (-7198, 76, -3536), (-4762, -1171, 100)]
    counter = 1
    locs = [(0, 0, 0)]
    while len(beacon_data) > 0:
        # print(len(beacon_data))
        add(beacon_data, beacons, locs)
    # print(locs)
    # print(beacons)
    # print(len(beacons))


def solve2(dat):
    data = dat["data"]
    scanners = [(0, 0, 0), [54, 1205, -34], [1129, 1313, -51], [-81, 2471, -53], [-64, 3691, -46], [96, 4931, 63], [-1156, 4793, -50], [-13, 4801, -1255], [-1162, 3686, -1163], [1183, 4812, -1209], [1208, 3707, -1217], [1316, 6106, -1274], [-18, 6093, -99], [-82, 6059, -1187], [106, 6008, -2451], [-1089, 4924, -2450], [-24, 7241, -2345], [49, 8511, -2335], [-1089, 3554, 18], [-1229, 4908, -1131], [79, 3580, -1213], [1202, 5975, -36], [2431, 6016, -115], [3677, 6107, -47], [-77, 7326, -1202], [40, 5990, 1167], [1267, 4757, -2436], [-1242, 3739, -2459], [76, 7198, -3536], [100, 4762, 1171]]
    max_dist = 0
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            max_dist = max(max_dist, abs(scanners[i][0] - scanners[j][0]) + abs(scanners[i][1] - scanners[j][1]) + abs(scanners[i][2] - scanners[j][2]))
    return max_dist


def main():
    day = 19
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
