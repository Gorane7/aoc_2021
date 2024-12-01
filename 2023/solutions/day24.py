from main import *
import random, math
# import matplotlib.pyplot as plt
import shelve
from sympy import Point, Line 

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def solve1(data):

    ints     = [extract_ints(x) for x in data]
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


    # SOLUTION
    i = 0
    s = ""
    d = {}
    u = set()
    l = []
    stones = []
    ans = 0
    for line in data:
        a, b = line.split(" @ ")
        pos = [int(x) for x in a.split(", ")]
        vel = [int(x) for x in b.split(", ")]
        stones.append((pos, vel))
    xy = [(a[0][0], a[0][1], a[1][0], a[1][1]) for a in stones]
    lsegs = []
    lines = []
    for pos, vel in stones:
        start = (pos[0], pos[1])
        slope = vel[1] / vel[0]
        at0 = start[1] - start[0] * slope
        #print(start, slope, at0)
        lines.append((slope, at0, start, (vel[0], vel[1])))
        #print(pos, vel, start, slope, at0)
        #p1 = Point(pos[0], pos[1])
        #p2 = Point(0, at0)
        #lines.append(Line(p1, p2))
    print()
    
    ans = 0
    l = 200000000000000
    h = 400000000000000
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            s1, b1, ss1, sp1 = lines[i]
            s2, b2, ss2, sp2 = lines[j]
            ds = s2 - s1  # Second line moves up this much more per x
            db = b1 - b2  # Second line needs to move up this much
            if ds == 0:
                continue
            intx = db / ds  # x needed to move should be move up needed divided by per x move
            inty1 = b1 + intx * s1
            inty2 = b2 + intx * s2
            if abs(inty1 - inty2) / ((inty1 + inty2) / 2) >= 0.0000001:
                print("ERROR: y1, y2 not equal")
                print((s1, b1), (s2, b2), intx, inty1, inty2)
                exit()
            timemoment1 = (intx - ss1[0]) / sp1[0]
            timemoment2 = (intx - ss2[0]) / sp2[0]
            #print(intx, inty1, timemoment1, timemoment2)
            if l <= intx <= h and l <= inty1 <= h and timemoment1 >= 0 and timemoment2 >= 0:
                ans += 1

    
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
    stones = []
    ans = 0
    for line in data:
        a, b = line.split(" @ ")
        pos = [int(x) for x in a.split(", ")]
        vel = [int(x) for x in b.split(", ")]
        stones.append((pos, vel))
    upto = 1
    dvx, dvy, dvz = stones[1][1][0] - stones[0][1][0], stones[1][1][1] - stones[0][1][1], stones[1][1][2] - stones[0][1][2]
    dx, dy, dz = stones[1][0][0] - stones[0][0][0], stones[1][0][1] - stones[0][0][1], stones[1][0][2] - stones[0][0][2]
    x0, y0, z0 = stones[0][0][0], stones[0][0][1], stones[0][0][2]
    vx0, vy0, vz0 = stones[0][1][0], stones[0][1][1], stones[0][1][2]
    x1, y1, z1 = stones[1][0][0], stones[1][0][1], stones[1][0][2]
    vx1, vy1, vz1 = stones[1][1][0], stones[1][1][1], stones[1][1][2]
    print(dx, dy, dz)
    print(dvx, dvy, dvz)
    #return 0
    while True:
        t0 = upto
        for t1 in range(upto + 1):
            if t0 == t1:
                continue
            t0p = x0 + t0 * vx0, y0 + t0 * vy0, z0 + t0 * vz0
            t1p = x1 + t1 * vx1, y1 + t1 * vy1, z1 + t1 * vz1
            dt = t1 - t0
            dp = t1p[0] - t0p[0], t1p[1] - t0p[1], t1p[2] - t0p[2]
            if dp[0] % dt != 0 or dp[1] % dt != 0 or dp[2] % dt != 0:
                continue
            dv = dp[0] // dt, dp[1] // dt, dp[2] // dt
            sp = t0p[0] - dv[0] * t0, t0p[1] - dv[1] * t0, t0p[2] - dv[2] * t0
            works = True
            for i in range(2, len(stones)):
                stp = stones[i][0][0], stones[i][0][1], stones[i][0][2]
                sv = stones[i][1][0], stones[i][1][1], stones[i][1][2]
            print(f"Comparing {t0} and {t1}, pos0: {t0p}, pos1: {t1p}, deltaPos: {dp}, velReq: {dv}, startPos: {sp}")

        
        t1 = upto
        for t0 in range(upto + 1):
            if t0 == t1:
                continue
            t0p = x0 + t0 * vx0, y0 + t0 * vy0, z0 + t0 * vz0
            t1p = x1 + t1 * vx1, y1 + t1 * vy1, z1 + t1 * vz1
            dt = t1 - t0
            dp = t1p[0] - t0p[0], t1p[1] - t0p[1], t1p[2] - t0p[2]
            if dp[0] % dt != 0 or dp[1] % dt != 0 or dp[2] % dt != 0:
                continue
            dv = dp[0] // dt, dp[1] // dt, dp[2] // dt
            sp = t0p[0] - dv[0] * t0, t0p[1] - dv[1] * t0, t0p[2] - dv[2] * t0
            print(f"Comparing {t0} and {t1}, pos0: {t0p}, pos1: {t1p}, deltaPos: {dp}, velReq: {dv}, startPos: {sp}")

        upto += 1


def main():
    day = 24
    data = parse_input(day)
    if data:
        print("Got data successfully")
    else:
        print("Error getting data")
    ans1, ans2 = None, None
    #ans1 = solve1([x for x in data])
    ans2 = solve2([x for x in data])
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
