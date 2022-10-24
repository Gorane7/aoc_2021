from main import *


def split(a):
    for i in range(len(a)):
        if isinstance(a[i], int) and a[i] >= 10:
            el = a[i]
            left, right = el // 2, el // 2
            right += el % 2
            a.pop(i)
            a.insert(i, "e")
            a.insert(i, right)
            a.insert(i, left)
            a.insert(i, "s")
            return True, a
    return False, a


def add_after(a, index):
    to_add = a[index]
    for i in range(index + 1, len(a)):
        if isinstance(a[i], int):
            a[i] += to_add
            return


def explode(a):
    last_number_index = -1
    nest_count = 0
    for i in range(len(a)):
        el = a[i]
        if el == "s":
            nest_count += 1
        elif el == "e":
            nest_count -= 1
        else:
            if nest_count >= 5:
                # TODO: Check if next is also number
                if last_number_index != -1:
                    a[last_number_index] += el
                add_after(a, i + 1)
                a.pop(i - 1)
                a.pop(i - 1)
                a.pop(i - 1)
                a[i - 1] = 0
                return True, a
            last_number_index = i
    return False, a


def reduce(a):
    could_explode, a = explode(a)
    if could_explode:
        return reduce(a)
    could_split, a = split(a)
    if could_split:
        return reduce(a)
    return a


def add(a, b):
    combined = ["s"]
    combined.extend(a)
    combined.extend(b)
    combined.append("e")
    return reduce(combined)


def my_parse(a, result):
    if isinstance(a, list):
        result.append("s")
        my_parse(a[0], result)
        my_parse(a[1], result)
        result.append("e")
        return result
    result.append(a)
    return result


def my_reverse_parse(a):
    a = [("[" if x == "s" else ("]" if x == "e" else str(x))) for x in a]
    a = list(",".join(a))
    counter = 0
    while counter < len(a):
        if a[counter] == ",":
            if a[counter - 1] == "[":
                a.pop(counter)
                continue
        counter += 1
    return eval("".join(a))


def magnitude(a):
    if isinstance(a, int):
        return a
    return 3 * magnitude(a[0]) + 2 * magnitude(a[1])


def solve1(dat):
    data = dat["data"]
    data = [eval(x) for x in data]
    data = [my_parse(x, []) for x in data]
    prev = data[0]
    # print(prev)
    for dat in data[1:]:
        prev = add(prev, dat)
    return magnitude(my_reverse_parse(prev))


def solve2(dat):
    data = dat["data"]
    data = [eval(x) for x in data]
    data = [my_parse(x, []) for x in data]
    best = 0
    for i in range(len(data)):
        for j in range(len(data)):
            best = max(best, magnitude(my_reverse_parse(add(data[i][:], data[j][:]))))
    return best


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
    ans1 = solve1(data)
    ans2 = solve2(data)
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
