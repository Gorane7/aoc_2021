import os
import time


def main():
    year = 2021
    for i in range(1, 26):
        if i in [19, 23, 24]:
            continue
        # 19 is horrendously slow and might now work anymore, also the code might be irrecoverably complicated
        # 23 is also horrendously slow, but is at least slightly readable
        # 24 was really hard to do programmatically, manual inspection of input was used to solve
        print(i)
        file = open(f"{year}/outputs/out{i}.txt")
        answers = [x.strip("\n") for x in file.readlines()]
        file.close()
        print(answers)
        start = time.time()
        os.chdir(f"{year}/solutions")
        os.system(f"python3 day{i}.py")
        os.chdir("../..")
        print(time.time() - start)
        print()


if __name__ == '__main__':
    main()
