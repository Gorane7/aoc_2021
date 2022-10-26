from main import *


def solve1(dat):
    data = dat["data"]
    numbers = [int(x) for x in data[0].split(",")]
    boards = []
    board = []
    for i in range(1, len(data)):
        # print(data[i])
        n = i - 1
        if n % 5 == 0:
            boards.append(board)
            board = []
        board.append([int(x) for x in data[i].split(" ") if len(x) > 0])
    boards.append(board)
    boards = boards[1:]
    boards = [make_board(x) for x in boards]

    has_bingo = False
    score_amount = 0
    victor_count = 0
    has_bingos = [False] * 100
    scores = [0] * 100
    # print(boards)
    # print(len(boards))
    for number in numbers:
        for i, board in enumerate(boards):
            # print(board)
            if has_bingos[i]:
                continue
            mark_board(board, number)
            if has_won(board[0]):
                score_amount = score(board, number)
                return score_amount


def score(board, number):
    total = 0
    for y, row in enumerate(board[1]):
        for x, value in enumerate(row):
            if not board[0][y][x]:
                total += value
    return total * number


def has_won(board):
    for i in range(len(board)):
        if all(board[i]):
            return True
        if all([row[i] for row in board]):
            return True

def mark_board(board, number):
    for y, row in enumerate(board[1]):
        for x, value in enumerate(row):
            if value == number:
                board[0][y][x] = True


def make_board(board):
    marks = []
    for i in board:
        marks.append([False for _ in i])
    return [marks, board]


def solve2(dat):
    data = dat["data"]
    numbers = [int(x) for x in data[0].split(",")]
    boards = []
    board = []
    for i in range(1, len(data)):
        # print(data[i])
        n = i - 1
        if n % 5 == 0:
            boards.append(board)
            board = []
        board.append([int(x) for x in data[i].split(" ") if len(x) > 0])
    boards.append(board)
    boards = boards[1:]
    boards = [make_board(x) for x in boards]

    has_bingo = False
    score_amount = 0
    victor_count = 0
    has_bingos = [False] * 100
    scores = [0] * 100
    # print(boards)
    # print(len(boards))
    for number in numbers:
        for i, board in enumerate(boards):
            # print(board)
            if has_bingos[i]:
                continue
            mark_board(board, number)
            if has_won(board[0]):
                score_amount = score(board, number)
                victor_count += 1
                # print(f"{victor_count}th victor found, he was {i} with {score_amount}")
                has_bingos[i] = True
                scores[i] = score_amount
                has_bingo = True
    return score_amount


def main():
    day = 4
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
