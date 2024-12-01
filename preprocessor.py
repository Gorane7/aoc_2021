

def process_line(line):
    if not line:
        return ("empty", line)
    if not {x for x in line}.difference(set("0123456789")):
        return ("int", int(line))
    return ("unknown", line)

def group_by(data, sep, main_type):
    groups = []
    cache = []
    for data_type, data_item in data:
        if data_type == sep:
            groups.append((("group", main_type), cache))
            cache = []
            continue
        cache.append(data_item)
    groups.append((("group", main_type), cache))
    return groups

def prep(data):
    data = [process_line(line) for line in data]
    classes = set([x[0] for x in data])
    if classes == {"int", "empty"}:
        data = group_by(data, "empty", "int")
    return data


def display(data):
    for line in data:
        print(line)


def main(year, day):
    file = open(f"{year}/inputs/in{day}.txt", "r")
    lines = [x.strip("\n") for x in file.readlines()]
    file.close()
    processed = prep(lines)
    display(processed)


if __name__ == '__main__':
    year = 2022
    day = 2
    main(year, day)
