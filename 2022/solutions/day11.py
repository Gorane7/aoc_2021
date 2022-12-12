from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


class Monkey:
    def __init__(self, items, operation, operation_nr, div_by, true_to, false_to):
        self.items = items
        if operation_nr == "old":
            self.operation = lambda x: x * x
        elif operation == "*":
            self.operation = lambda x: x * int(operation_nr)
        else:
            self.operation = lambda x: x + int(operation_nr)
        self.div_by = div_by
        self.true_to = true_to
        self.false_to = false_to
        self.inspection_amount = 0


def solve1(data):

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
    monkeys = {}
    for i in range((len(data) + 1) // 7):
        nr = i
        items = [int(x) for x in data[i * 7 + 1].split(": ")[1].split(", ")]
        op_op = data[i * 7 + 2].split(" ")[-2]
        op_am = data[i * 7 + 2].split(" ")[-1]
        div_by = int(data[i * 7 + 3].split(" ")[-1])
        true_to = int(data[i * 7 + 4].split(" ")[-1])
        false_to = int(data[i * 7 + 5].split(" ")[-1])
        monkeys[nr] = Monkey(items, op_op, op_am, div_by, true_to, false_to)
    for nr in range(10000):
        print(nr / 10000)
        for i in range(8):
            while len(monkeys[i].items) > 0:
                item = monkeys[i].items[0]
                monkeys[i].items = monkeys[i].items[1:]
                item = monkeys[i].operation(item)
                item = item % 9699690
                if item % monkeys[i].div_by == 0:
                    monkeys[monkeys[i].true_to].items.append(item)
                else:
                    monkeys[monkeys[i].false_to].items.append(item)
                monkeys[i].inspection_amount += 1
    inspections = [x.inspection_amount for x in monkeys.values()]
    print(inspections)
    for ini in ints:
        pass

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
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE


def main():
    day = 11
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    ans1 = solve1([x for x in data])
    ans2 = solve2([x for x in data])
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")


if __name__ == '__main__':
    main()
