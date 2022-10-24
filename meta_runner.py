import os
import time


def main():
    for i in range(10, 13):
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
