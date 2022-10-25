import os
import time


def main():
    for i in range(25, 26):
        # 19 is horrendously slow and might now work anymore, also the code might be irrecoverably complicated
        # 23 is also horrendously slow, but is at least slightly readable
        # 24 was really hard to do programmatically, manual inspection of input was used to solve
        print(i)
        file = open(f"outputs/out{i}.txt")
        answers = [x.strip("\n") for x in file.readlines()]
        file.close()
        print(answers)
        start = time.time()
        os.system(f"python3 day{i}.py")
        print(time.time() - start)
        print()


if __name__ == '__main__':
    main()
