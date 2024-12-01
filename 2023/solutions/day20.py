from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
import cv2
import numpy as np

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def solve1(data):

    # first  = map_lines(data[:1], [int], ",")
    parsed   = map_lines(data, [str])
    # parsed = map_lines(data, [int])
    # parsed = my_map(parsed, lambda x: [int(a) for a in x])
    # parsed = my_map(parsed, lambda x: (x[0].split(","), x[2].split(",")))
    # parsed = my_map(parsed, lambda x: [(a[0].split(","), a[1].split(",")) for a in x])
    parsed   = my_map(parsed, lambda x: x)
    data     = my_map(data, lambda x: x)
    #data    = my_map(data, lambda x: [int(a) for a in x.split(" ")])
    print()
    print("!!!SAMPLE INPUT!!!")
    [print(x) for x in data[:20]]
    print("!!!END SAMPLE INPUT!!!")
    print()


    ms = {}
    # SOLUTION
    flipflops = {}
    mems = {}
    for line in data:
        a, b = line.split(" -> ")
        if a == "broadcaster":
            broadcaster = b.split(", ")
            continue
        if a[0] == "%":
            ms[a[1:]] = ("%", b.split(", "))
            flipflops[a[1:]] = False
            continue
        ms[a[1:]] = ("&", b.split(", "))
        mems[a[1:]] = {}
    for key, value in ms.items():
        for dest in value[1]:
            if dest in mems.keys():
                mems[dest][key] = "low"
    tlow = 0
    thigh = 0
    for i in range(1000):
        queue = [("low", "broadcaster", "button")]
        qc = 0
        while qc < len(queue):
            t, dest, f = queue[qc]
            qc += 1
            if dest == "broadcaster":
                for d in broadcaster:
                    queue.append((t, d, dest))
                continue
            if dest not in ms.keys():
                continue
            bt, dests = ms[dest]
            if bt == "%":
                if t == "high":
                    continue
                if flipflops[dest]:
                    for d in dests:
                        queue.append(("low", d, dest))
                    flipflops[dest] = False
                else:
                    for d in dests:
                        queue.append(("high", d, dest))
                    flipflops[dest] = True
                continue
            mems[dest][f] = t
            #print(mems[dest].values())
            if len([x for x in mems[dest].values()]) == len([x for x in mems[dest].values() if x == "high"]):
                for d in dests:
                    queue.append(("low", d, dest))
            else:
                for d in dests:
                    queue.append(("high", d, dest))
        print(len([x for x in queue if x[0] == "low"]), len([x for x in queue if x[0] == "high"]))
        tlow += len([x for x in queue if x[0] == "low"])
        thigh += len([x for x in queue if x[0] == "high"])
            

    # END SOLUTION

    my_shelf = shelve.open("shelf.tmp",'n')
    for key in dir():
        try:
            my_shelf[key] = locals()[key]
        except:
            print(f"ERROR shelving {key}")
    my_shelf.close()
    return tlow * thigh


def solve3(data):
    ms = {}
    # SOLUTION
    flipflops = {}
    mems = {}
    for line in data:
        a, b = line.split(" -> ")
        if a == "broadcaster":
            broadcaster = b.split(", ")
            continue
        if a[0] == "%":
            ms[a[1:]] = ("%", b.split(", "))
            flipflops[a[1:]] = False
            continue
        ms[a[1:]] = ("&", b.split(", "))
        mems[a[1:]] = {}
    for key, value in ms.items():
        for dest in value[1]:
            if dest in mems.keys():
                mems[dest][key] = "low"
    
    nodes = {key: (random.random() * 1000, random.random() * 1000) for key in ms.keys()}
    nodes["rx"] = (random.random() * 1000, random.random() * 1000)
    while True:
        img = np.ones([1000, 1000, 3], dtype=np.uint8) * 255
        for key in ms.keys():
            vals = ms[key][1]
            l1 = (int(nodes[key][0]), int(nodes[key][1]))
            for val in vals:
                l2 = (int(nodes[val][0]), int(nodes[val][1]))
                cv2.line(img, l1, l2, (0, 255, 0), 2)

        for name, loc in nodes.items():
            print(name, loc)
            cv2.circle(img, (int(loc[0]), int(loc[1])), 5, (255, 0, 0), 2)
        cv2.imshow("img", img)
        if cv2.waitKey(0) == 27:
            break


def solve2(data):
    my_shelf = shelve.open("shelf.tmp")
    for key in my_shelf:
        globals()[key] = my_shelf[key]
    my_shelf.close()

    # SOLUTION HERE
    ms = {}
    # SOLUTION
    flipflops = {}
    mems = {}
    watching = ["dd", "fh", "xp", "fc"]
    for line in data:
        a, b = line.split(" -> ")
        if a == "broadcaster":
            broadcaster = b.split(", ")
            continue
        if a[0] == "%":
            ms[a[1:]] = ("%", b.split(", "))
            flipflops[a[1:]] = False
            continue
        ms[a[1:]] = ("&", b.split(", "))
        mems[a[1:]] = {}
    for key, value in ms.items():
        for dest in value[1]:
            if dest in mems.keys():
                mems[dest][key] = "low"
    tlow = 0
    thigh = 0
    for i in range(100000000000):
        crx = 0
        queue = [("low", "broadcaster", "button")]
        qc = 0
        while qc < len(queue):
            t, dest, f = queue[qc]
            qc += 1
            if dest == "broadcaster":
                for d in broadcaster:
                    queue.append((t, d, dest))
                continue
            if dest in watching and t == "high":
                print(f"{dest} sent high at {i}")
            if dest not in ms.keys():
                #print(t, dest, f)
                if t == "low":
                    #return i + 1
                    crx += 1
                continue
            bt, dests = ms[dest]
            if bt == "%":
                if t == "high":
                    continue
                if flipflops[dest]:
                    for d in dests:
                        queue.append(("low", d, dest))
                    flipflops[dest] = False
                else:
                    for d in dests:
                        queue.append(("high", d, dest))
                    flipflops[dest] = True
                continue
            mems[dest][f] = t
            #print(mems[dest].values())
            if len([x for x in mems[dest].values()]) == len([x for x in mems[dest].values() if x == "high"]):
                for d in dests:
                    queue.append(("low", d, dest))
            else:
                for d in dests:
                    queue.append(("high", d, dest))
        #print(len([x for x in queue if x[0] == "low"]), len([x for x in queue if x[0] == "high"]))
        tlow += len([x for x in queue if x[0] == "low"])
        thigh += len([x for x in queue if x[0] == "high"])
        if crx == 1:
            return i + 1


def main():
    day = 20
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    ans1 = solve1([x for x in data])
    ans2 = solve2([x for x in data])
    solve3([x for x in data])
    exit()
    print(f"Answer a: {ans1}")
    print(f"Answer b: {ans2}")

    testdata = parse_input(-1)
    if testdata:
        ans1t = solve1([x for x in testdata])
        ans2t = solve2([x for x in testdata])
        print(f"Answer a: {ans1}")
        print(f"Answer b: {ans2}")
        print(f"Test a: {ans1t}")
        print(f"Test b: {ans2t}")


if __name__ == '__main__':
    main()
