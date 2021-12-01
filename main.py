import requests

# CONSTANTS
YEAR = 2020


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
    print("Problem, can't parse line with splits yet")
    exit()


def save_input(day, lines):
    file = open(f"inputs/in{day}.txt", "w")
    file.write("\n".join(lines))
    file.close()


def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {
        "_ga": "GA1.2.14223148.1638045100",
        "session": "53616c7465645f5f4802c58532988d34dac42590f2556e11734e96b0c39f9e5c65438a7be2ad722c82f4333ee1db3078",
        "_gid": "GA1.2.1672151336.1638134874"
    }
    ans = requests.get(url, cookies=cookies)
    print(ans.status_code)
    if ans.status_code == 200:
        return [x for x in ans.text.split("\n") if len(x) > 0]
    return []


def parse_input(day, input_format):
    file = open(f"inputs/in{day}.txt", "r")
    lines = [x.strip("\n") for x in file.readlines()]
    file.close()
    if len(lines) == 0:
        lines = get_input(YEAR, day)
        save_input(day, lines)
    return parse_lines(lines, input_format)


if __name__ == '__main__':
    print(get_input(2020, 2))
