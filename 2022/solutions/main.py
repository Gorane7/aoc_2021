import requests
import os

# CONSTANTS
YEAR = 2022


def smart_map_lines(lines, delim=" "):
    new_lines = []
    for line in lines:
        splitted = line.split(delim)
        for i in range(len(splitted)):
            pass
    return new_lines


def map_lines(lines, functions, delim=" "):
    new_lines = []
    for a, line in enumerate(lines):
        new_line = line.split(delim)
        if a == 0 and len(functions) != len(new_line):
            print("WARNING: function list length, not equal to line element amount")
        out_line = []
        for i in range(len(new_line)):
            if len(new_line[i]) > 0:
                out_line.append(functions[i % len(functions)](new_line[i]))
        if len(out_line) == 1:
            new_lines.append(out_line[0])
        else:
            new_lines.append(tuple(out_line))
    return new_lines


def my_map(inp_list, function):
    return [function(x) for x in inp_list]


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
        "_ga": "GA1.2.47538840.1659169507",
        "session": "53616c7465645f5f56e50a04e0e6a8f683845e43a9162d67a82b09ac8a8aa5400ff9401d28c4251615f1ddbeb717f64fce2a232ca79b12fe71016a6eb1b2724b",
        "_gid": "GA1.2.958522239.1670129049"
    }
    headers = {
        "User-agent": "A python script by kristjankv32@gmail.com ... Will upload script to github and link soon"
    }
    ans = requests.get(url, headers=headers, cookies=cookies)
    print(ans.status_code)
    if ans.status_code == 200:
        return [x for x in ans.text.split("\n")]
    return []


def parse_input(day):
    lines = []
    if os.path.exists(f"../inputs/in{day}.txt"):
        file = open(f"../inputs/in{day}.txt", "r")
        lines = [x.strip("\n") for x in file.readlines()]
        file.close()
    if len(lines) == 0:
        lines = get_input(YEAR, day)
        save_input(day, lines)
    return lines


if __name__ == '__main__':
    print(get_input(2021, 2))
