import requests
import os

# CONSTANTS
YEAR = 2021


def parse_lines(lines, input_format):
    counter = 0
    parsed = {}
    for amount, parser in input_format:
        lines = parse(amount, parser, lines, parsed)
    return parsed


def parse(amount, parser, lines, parsed):
    if amount == "...":
        this_parse = [parse_line(line, parser) for line in lines]
        parsed["data"] = this_parse
        return []


def parse_line(line, parser):
    elements = []
    splits = []
    cache = ""
    for letter in parser:
        if letter == "{":
            if cache != "":
                splits.append(cache)
            cache = ""
        elif letter == "}":
            if cache != "":
                elements.append(cache)
            cache = ""
        else:
            cache += letter
    if len(splits) == 0:
        if elements[0] == "int":
            return int(line)
        if elements[0] == "string":
            return line
    elif len(set(splits)) == 1:
        split = line.split(splits[0])
        for i in range(len(split)):
            if elements[i] == "int":
                split[i] = int(split[i])
            elif elements[i] == "string":
                split[i] = split[i]
        return split
    print("Problem, can't parse line with splits yet")
    exit()


def save_input(day, lines):
    file = open(f"../inputs/in{day}.txt", "w")
    file.write("\n".join(lines))
    file.close()


def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {
        "_gat": "1",
        "_ga": "GA1.2.1668813612.1666544999",
        "session": "53616c7465645f5fff1738b41a2cf505ad51e2834adf62d5668670228021b7efc1ed1bdc20474202dc3178ca00223ce1356e368946e5665d0a4c93a834e6074e",
        "_gid": "GA1.2.743798007.1666544999"
    }
    ans = requests.get(url, cookies=cookies)
    print(ans.status_code)
    if ans.status_code == 200:
        return [x for x in ans.text.split("\n") if len(x) > 0]
    return []


def parse_input(day, input_format):
    lines = []
    if os.path.exists(f"../inputs/in{day}.txt"):
        file = open(f"../inputs/in{day}.txt", "r")
        lines = [x.strip("\n") for x in file.readlines()]
        file.close()
    if len(lines) == 0:
        lines = get_input(YEAR, day)
        save_input(day, lines)
    return parse_lines(lines, input_format)


if __name__ == '__main__':
    print(get_input(2020, 2))
