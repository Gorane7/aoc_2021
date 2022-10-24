from main import *

def hex_to_bin(hex):
    maps = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    return maps[hex]


def parse_literal(bits, level, version):
    literal = ""
    at = 0
    while True:

        next_bits = bits[at:at + 5]
        at += 5
        literal += next_bits[1:]
        if next_bits[0] == "0":
            # print(f"{' ' * level}Parsed literal {int(literal, 2)}")
            return {"literal": literal, "version": version}, at + 6


def parse_bits(bits, level):
    # print(f"{' ' * level}Parsing {bits[:6]} {bits[6:]}")
    version = bits[:3]
    type_id = bits[3:6]

    if type_id == "100":
        return parse_literal(bits[6:], level, version)
    # print("Printing ", type_id, bits)
    length_type = bits[6]
    at = 7
    # print(bits[at:])
    if length_type == "0":

        length_bits = int(bits[at:at + 15], 2)
        at += 15
        parsed = 0
        sub_packets = []
        # print(f"{' ' * level}Looking for sub packet of length {length_bits}")
        while parsed < length_bits:
            sub_packet, parsed_here = parse_bits(bits[at + parsed:], level + 1)
            parsed += parsed_here
            sub_packets.append(sub_packet)
        at += parsed
    else:
        length_bits = int(bits[at:at + 11], 2)
        at += 11
        sub_packets = []
        # print(f"{' ' * level}Looking for {length_bits} sub packets")
        for i in range(length_bits):
            sub_packet, parsed_here = parse_bits(bits[at:], level + 1)
            at += parsed_here
            sub_packets.append(sub_packet)
    return {"type": "op", "type id": int(type_id, 2), "version": version, "sub": sub_packets}, at


def print_packet(packets, level):
    if "literal" in packets.keys():
        # print(f"{' ' * level}Literal: {packets['literal']}")
        return int(packets["version"], 2)
    # print(f"{' ' * level}Operator: {packets['version']}")
    # print(f"{' ' * level}Sub packets ")
    total = int(packets["version"], 2)
    for packet in packets["sub"]:
        total += print_packet(packet, level + 1)
    return total


def calculate_packet(packets, level):
    if "literal" in packets.keys():
        return int(packets["literal"], 2)
    if packets["type id"] == 0:
        return sum([calculate_packet(packet, level + 1) for packet in packets["sub"]])
    if packets["type id"] == 1:
        total = 1
        for packet in packets["sub"]:
            total *= calculate_packet(packet, level + 1)
        return total
    if packets["type id"] == 2:
        return min([calculate_packet(packet, level + 1) for packet in packets["sub"]])
    if packets["type id"] == 3:
        return max([calculate_packet(packet, level + 1) for packet in packets["sub"]])
    if packets["type id"] == 5:
        value1 = calculate_packet(packets["sub"][0], level + 1)
        value2 = calculate_packet(packets["sub"][1], level + 1)
        return 1 if value1 > value2 else 0
    if packets["type id"] == 6:
        value1 = calculate_packet(packets["sub"][0], level + 1)
        value2 = calculate_packet(packets["sub"][1], level + 1)
        return 1 if value1 < value2 else 0
    if packets["type id"] == 7:
        value1 = calculate_packet(packets["sub"][0], level + 1)
        value2 = calculate_packet(packets["sub"][1], level + 1)
        return 1 if value1 == value2 else 0



def solve1(dat):
    data = dat["data"]
    data = "".join([hex_to_bin(x) for x in data[0]])
    # print(data)
    packets, amount = parse_bits(data, 0)
    # print()
    version_sum = print_packet(packets, 0)
    return version_sum


def solve2(dat):
    data = dat["data"]
    data = "".join([hex_to_bin(x) for x in data[0]])
    # print(data)
    packets, amount = parse_bits(data, 0)
    # print()
    return calculate_packet(packets, 0)


def main():
    day = 16
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
