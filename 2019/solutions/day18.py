from main import *


def remove_key(chr, world):
    upper = chr.upper()
    new_map = []
    for line in world:
        new_line = []
        for ch in line:
            if ch in upper + chr:
                new_line.append(".")
                continue
            new_line.append(ch)
        new_map.append("".join(new_line))
    return new_map


def solve1(dat):
    data = dat["data"]
    letters = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch in "#.@":
                if ch == "@":
                    sx, sy = x, y
                continue
            if ch.islower() and ch not in letters:
                letters.append(ch)
    letters = "".join(sorted(letters))
    worlds = {"": data}
    stack_in = []
    stack_out = []
    stack_in.append(((sx, sy, ""), 0))
    visited = set()
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    size_x = len(data[0])
    size_y = len(data)
    i = 0
    while stack_in or stack_out:
        i += 1
        if i % 100000 == 0:
            pass
            # print(len(stack_in) + len(stack_out))
        if not stack_out:
            while stack_in:
                stack_out.append(stack_in.pop())
        loc, steps = stack_out.pop()
        x, y, world = loc
        if (x, y, world) in visited:
            continue
        visited.add((x, y, world))
        # print(x, y, world, steps)
        for dx, dy in deltas:
            if 0 <= x + dx < size_x and 0 <= y + dy < size_y:
                if worlds[world][y + dy][x + dx] == "#":
                    continue
                if worlds[world][y + dy][x + dx].isupper():
                    continue
                new_world = world
                if worlds[world][y + dy][x + dx].islower():
                    new_world = "".join(sorted([ch for ch in world] + [worlds[world][y + dy][x + dx]]))
                    if new_world == letters:
                        return steps + 1
                    if new_world not in worlds.keys():
                        worlds[new_world] = remove_key(worlds[world][y + dy][x + dx], worlds[world])
                stack_in.append(((x + dx, y + dy, new_world), steps + 1))
    return letters, (sx, sy)


def get_available_keys(world, starts, deltas, size_x, size_y):
    keys = []
    for i, start in enumerate(starts):
        stack = []
        stack.append(start)
        visited = set()
        while stack:
            x, y = stack.pop()
            for dx, dy in deltas:
                if 0 <= x + dx < size_x and 0 <= y + dy < size_y:
                    if world[y + dy][x + dx] == "#":
                        continue
                    if world[y + dy][x + dx].isupper():
                        continue
                    if (x + dx, y + dy) in visited:
                        continue
                    visited.add((x + dx, y + dy))
                    if world[y + dy][x + dx].islower():
                        keys.append((world[y + dy][x + dx], i))
                        continue
                    stack.append((x + dx, y + dy))
    return keys


def solve2(dat):
    data = dat["data"]
    sx, sy = None, None
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "@":
                sx, sy = x, y
                break
        if sx is not None:
            break
    data = [[ch for ch in line] for line in data]
    starts = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                data[sy + dy][sx + dx] = "#"
                continue
            if abs(dx) == abs(dy):
                data[sy + dy][sx + dx] = "@"
                starts.append((sy + dy, sx + dx))
                continue
            data[sy + dy][sx + dx] = "#"
    data = ["".join(line) for line in data]

    letters = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch in "#.@":
                continue
            if ch.islower() and ch not in letters:
                letters.append(ch)
    letters = "".join(sorted(letters))

    visited = set()
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    size_x = len(data[0])
    size_y = len(data)

    stack_in = []
    stack_out = []
    worlds = {"": data}
    for target, robot in get_available_keys(data, starts, deltas, size_x, size_y):
        print(target, robot)


def main():
    day = 18
    basic = [("...", "{string}")]
    ints = [("...", "{int}")]
    input_format = basic
    data = parse_input(day, input_format)
    if data["data"]:
        print("Got data successfully")
    else:
        print("Error getting data")
    # ans1 = solve1(data)
    ans1 = None
    ans2 = solve2(data)
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
