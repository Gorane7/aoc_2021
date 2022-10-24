import sys
# sys.setrecursionlimit(25000)
import random

from main import *

skip = []
end_after = 7

def parse_region(x):
    sp1 = x.split("=")[1]
    sp = sp1.split("..")
    return int(sp[0]), int(sp[1])

def solve1(dat):
    data = dat["data"]
    cubes = []
    delta = 50
    for i in range(-50, 51):
        row1 = []
        for j in range(-50, 51):
            row2 = []
            for k in range(-50, 51):
                row2.append(0)
            row1.append(row2)
        cubes.append(row1)
    for i, line in enumerate(data):
        if i in skip:
            continue
        sp1 = line.split(" ")
        command = sp1[0]
        sp2 = sp1[1].split(",")
        x, y, z = sp2[0], sp2[1], sp2[2]
        x, y, z = parse_region(x), parse_region(y), parse_region(z)
        for dx in range(max(x[0], -50) + 50, min(x[1] + 1, 51) + 50):
            for dy in range(max(y[0], -50) + 50, min(y[1] + 1, 51) + 50):
                for dz in range(max(z[0], -50) + 50, min(z[1] + 1, 51) + 50):
                    if command == "on":
                        cubes[dx][dy][dz] = 1
                    else:
                        cubes[dx][dy][dz] = 0
        if i == end_after:
            break

    total = 0
    for row1 in cubes:
        for row2 in row1:
            for value in row2:
                total += value
    return total


class Cube:
    def __init__(self, xs, xe, ys, ye, zs, ze, on):
        self.xs = xs
        self.xe = xe
        self.ys = ys
        self.ye = ye
        self.zs = zs
        self.ze = ze
        self.on = on

    def get_area(self):
        return (1 + self.xe - self.xs) * (1 + self.ye - self.ys) * (1 + self.ze - self.zs)

    def get_values(self, index):
        if index == 0:
            return self.xs, self.xe
        if index == 1:
            return self.ys, self.ye
        return self.zs, self.ze

    def set_values(self, index, s, e):
        if index == 0:
            self.xs, self.xe = s, e
        elif index == 1:
            self.ys, self.ye = s, e
        else:
            self.zs, self.ze = s, e
        return self

    @staticmethod
    def from_cube(cube):
        return Cube(cube.xs, cube.xe, cube.ys, cube.ye, cube.zs, cube.ze, cube.on)

    def __str__(self):
        return f"[({self.xs}...{self.xe}), ({self.ys}...{self.ye}), ({self.zs}...{self.ze})]"

    def __repr__(self):
        return str(self)


def has_overlap(cube1, cube2):
    cond1 = cube1.xe < cube2.xs
    cond2 = cube2.xe < cube1.xs
    cond3 = cube1.ye < cube2.ys
    cond4 = cube2.ye < cube1.ys
    cond5 = cube1.ze < cube2.zs
    cond6 = cube2.ze < cube1.zs
    return not (cond1 or cond2 or cond3 or cond4 or cond5 or cond6)


def split_along(index, values, cube):
    c1, c2 = cube.get_values(index)
    # print(f"Parsing cube {cube}, values are {values}, with index {index} and cube values are {c1} and {c2}")
    if c1 == values[0]:
        if c2 == values[1]:
            return [Cube.from_cube(cube), None, None]
        if c2 == values[2]:
            cube_a = Cube.from_cube(cube).set_values(index, values[0], values[1] - 1) if values[1] > values[0] else None
            return [cube_a, Cube.from_cube(cube).set_values(index, values[1], values[2]), None]
        if c2 == values[3]:
            cube_a = Cube.from_cube(cube).set_values(index, values[0], values[1] - 1) if values[1] > values[0] else None
            cube_c = Cube.from_cube(cube).set_values(index, values[2] + 1, values[3]) if values[3] > values[2] else None
            return [cube_a, Cube.from_cube(cube).set_values(index, values[1], values[2]), cube_c]
    if c1 == values[1]:
        if c2 == values[2]:
            return [None, Cube.from_cube(cube), None]
        if c2 == values[3]:
            cube_c = Cube.from_cube(cube).set_values(index, values[2] + 1, values[3]) if values[3] > values[2] else None
            return [None, Cube.from_cube(cube).set_values(index, values[1], values[2]), cube_c]
    if c1 == values[2]:
        if c2 == values[3]:
            return [None, None, Cube.from_cube(cube)]


def combine_cubes(cube1, cube2, split_index):
    if cube1 is None and cube2 is None:
        return []
    if cube1 is None:
        return [cube2]
    if cube2 is None:
        return [cube1]
    if not has_overlap(cube1, cube2):
        return [cube1, cube2]
    if split_index == 0:
        values = sorted([cube1.xs, cube1.xe, cube2.xs, cube2.xe])
    elif split_index == 1:
        values = sorted([cube1.ys, cube1.ye, cube2.ys, cube2.ye])
    else:
        values = sorted([cube1.zs, cube1.ze, cube2.zs, cube2.ze])
    cube1 = split_along(split_index, values, cube1)
    cube2 = split_along(split_index, values, cube2)
    if split_index == 2:
        pairs = []
        should_ret = [cube for cube in cube1 + cube2 if cube is not None]
        actual_ret = []
        for cube in should_ret:
            if (cube.zs, cube.ze) in pairs:
                continue
            pairs.append((cube.zs, cube.ze))
            actual_ret.append(cube)
        # print(f"Should return {actual_ret}")
        return actual_ret
    return_list = []
    for i in range(3):
        return_list += combine_cubes(cube1[i], cube2[i], split_index + 1)
    return merge_cubes(return_list)


def can_be_merged(cube1, cube2):
    if cube1.get_values(0) == cube2.get_values(0):
        if cube1.get_values(1) == cube2.get_values(1):
            if cube1.ze + 1 == cube2.zs or cube2.ze + 1 == cube1.zs:
                return 2
            return -1
        if cube1.get_values(2) == cube2.get_values(2):
            if cube1.ye + 1 == cube2.ys or cube2.ye + 1 == cube1.ys:
                return 1
            return -1
        return -1
    if cube1.get_values(1) == cube2.get_values(1):
        if cube1.get_values(2) == cube2.get_values(2):
            if cube1.xe + 1 == cube2.xs or cube2.xe + 1 == cube1.xs:
                return 0
            return -1
        return -1
    return -1


def merge(cube_list, i, j, index):
    cube2 = cube_list.pop(j)
    cube1 = cube_list.pop(i)
    new_cube = Cube.from_cube(cube1)
    s = min(min(cube1.get_values(index)), min(cube2.get_values(index)))
    e = max(max(cube1.get_values(index)), max(cube2.get_values(index)))
    new_cube.set_values(index, s, e)
    cube_list.append(new_cube)
    return cube_list


def merge_cubes(cube_list):
    for i in range(len(cube_list)):
        for j in range(i + 1, len(cube_list)):
            merge_index = can_be_merged(cube_list[i], cube_list[j])
            if merge_index >= 0:
                return merge_cubes(merge(cube_list, i, j, merge_index))
    return cube_list


def solve_overlap(cubes, level):
    if not cubes:
        return []
    # print(f"Recursion level {level} and have {len(cubes)} cubes")
    overlap = []
    no_overlap = []
    overlapping = [False] * len(cubes)
    found = False
    si = None
    sj = None
    for i in range(len(cubes)):
        for j in range(i + 1, len(cubes)):
            if has_overlap(cubes[i], cubes[j]):
                if not found:
                    found = True
                    si = i
                    sj = j
                overlapping[i] = True
                overlapping[j] = True
    for i in range(len(cubes)):
        if i == si or i == sj:
            continue
        elif overlapping[i]:
            overlap.append(cubes[i])
        else:
            no_overlap.append(cubes[i])
    if found:
        overlap = overlap + combine_cubes(cubes[si], cubes[sj], 0)
    # print(f"For recursion overlap found was {found}")
    return no_overlap + solve_overlap(overlap, level + 1)


def solve2_old(dat):
    data = dat["data"]
    cubes = []
    for i, line in enumerate(data):
        if i in skip:
            continue
        sp1 = line.split(" ")
        command = sp1[0]
        sp2 = sp1[1].split(",")
        x, y, z = sp2[0], sp2[1], sp2[2]
        x, y, z = parse_region(x), parse_region(y), parse_region(z)
        xs, xe = x
        ys, ye = y
        zs, ze = z
        this_cube = Cube(xs, xe, ys, ye, zs, ze, True if command == "on" else False)

        cubes.append(this_cube)
        cubes = solve_overlap(cubes, 0)

        cubes = [cube for cube in cubes if has_overlap(cube, this_cube) and command == "on" or not has_overlap(cube, this_cube)]

        print(f"After {i}th step, have {len(cubes)} cubes.")
        if i == end_after:
            for cube in cubes:
                print(cube)
            break

    total = 0
    for cube in cubes:
        if cube.on:
            total += cube.get_area()
    return total


def line_to_cube(line):
    sp1 = line.split(" ")
    command = sp1[0]
    sp2 = sp1[1].split(",")
    x, y, z = sp2[0], sp2[1], sp2[2]
    x, y, z = parse_region(x), parse_region(y), parse_region(z)
    xs, xe = x
    ys, ye = y
    zs, ze = z
    return [command, xs, xe, ys, ye, zs, ze]


def filter_cubes(start, end, data, ind):
    filtered = []
    for cube in data:
        if cube[ind * 2 + 1] >= end:
            continue
        if cube[ind * 2 + 2] < start:
            continue
        new_start = max(start, cube[ind * 2 + 1])
        new_end = min(end - 1, cube[ind * 2 + 2])
        copy = cube[:]
        copy[ind * 2 + 1] = new_start
        copy[ind * 2 + 2] = new_end
        filtered.append(copy)
    return filtered


def solve2(dat):
    data = dat["data"]
    data = [line_to_cube(line) for line in data]
    x_axes = sorted(list(set([x[1] for x in data] + [x[2] + 1 for x in data])))
    x_bins = [(x_axes[i], x_axes[i + 1]) for i in range(len(x_axes) - 1)]
    x_map = {bin_key: filter_cubes(bin_key[0], bin_key[1], data, 0) for bin_key in x_bins}
    total = 0
    for key, cubes in x_map.items():
        y_axes = sorted(list(set([x[3] for x in cubes] + [x[4] + 1 for x in cubes])))
        y_bins = [(y_axes[i], y_axes[i + 1]) for i in range(len(y_axes) - 1)]
        y_map = {bin_key: filter_cubes(bin_key[0], bin_key[1], cubes, 1) for bin_key in y_bins}
        # print(f"x range {key} has {len(cubes)} cubes and made y split with {len(y_map.items())} subranges")
        for key2, cubes2 in y_map.items():
            z_axes = sorted(list(set([x[5] for x in cubes2] + [x[6] + 1 for x in cubes2])))
            z_bins = [(z_axes[i], z_axes[i + 1]) for i in range(len(z_axes) - 1)]
            z_map = {bin_key: filter_cubes(bin_key[0], bin_key[1], cubes2, 2) for bin_key in z_bins}
            for key3, cubes3 in z_map.items():
                status = 'off'
                area = 0
                for subcube in cubes3:
                    area = (subcube[2] - subcube[1] + 1) * (subcube[4] - subcube[3] + 1) * (subcube[6] - subcube[5] + 1)
                    status = subcube[0]
                if status == 'on':
                    total += area
                # print()
            # print(f"    y range {key2} has {len(cubes2)} cubes and made z split with {len(z_map.items())} subranges, total so far: {total}")
        # print(len(y_map.items()))
    return total


def main():
    day = 22
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
