from main import *
import heapq


def solve1(dat):
    data = dat["data"]
    x_size = len(data[0])
    y_size = len(data)
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, 0, 0))
    explored = set()
    while len(heap) > 0:
        length, x, y = heapq.heappop(heap)
        if (x, y) in explored:
            continue
        explored.add((x, y))

        if x + 1 < x_size:
            heapq.heappush(heap, (length + int(data[y][x + 1]), x + 1, y))
        if y + 1 < y_size:
            heapq.heappush(heap, (length + int(data[y + 1][x]), x, y + 1))
        if x - 1 > 0:
            heapq.heappush(heap, (length + int(data[y][x - 1]), x - 1, y))
        if y - 1 > 0:
            heapq.heappush(heap, (length + int(data[y - 1][x]), x, y - 1))
        if x + 1 == x_size and y + 1 == y_size:
            return length


def solve2(dat):
    data = dat["data"]
    orig_len = len(data)
    # print(len(data[0]), len(data))
    for i in range(len(data)):
        temp = data[i]
        for mod in range(1, 5):
            for el in data[i]:
                temp += str((int(el) + mod - 1) % 9 + 1)
        data[i] = temp
    for mod in range(1, 5):
        for i in range(orig_len):
            row = ""
            for j, el in enumerate(data[i]):
                row += str((int(el) + mod - 1) % 9 + 1)
            data.append(row)
    for line in data:
        # print(line)
        pass
    # print(len(data[0]), len(data))
    x_size = len(data[0])
    y_size = len(data)
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, 0, 0))
    explored = set()
    while len(heap) > 0:
        length, x, y = heapq.heappop(heap)
        if (x, y) in explored:
            continue
        explored.add((x, y))

        if x + 1 < x_size:
            heapq.heappush(heap, (length + int(data[y][x + 1]), x + 1, y))
        if y + 1 < y_size:
            heapq.heappush(heap, (length + int(data[y + 1][x]), x, y + 1))
        if x - 1 > 0:
            heapq.heappush(heap, (length + int(data[y][x - 1]), x - 1, y))
        if y - 1 > 0:
            heapq.heappush(heap, (length + int(data[y - 1][x]), x, y - 1))
        if x + 1 == x_size and y + 1 == y_size:
            return length


def main():
    day = 15
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
