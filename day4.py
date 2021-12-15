import requests


def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/4/input', cookies=dict(session=cookie)).text[:-1]

    split_data = data.split("\n\n")

    return split_data


def day4_part1():
    print(f"day4_part1")
    data = get_input()
    bingo_stream = list(map(lambda i: int(i), data[0].split(",")))

    boards = list(map(lambda p: [list(map(lambda b: int(b), list(filter(lambda z: z != "", y.split(" "))))) for y in p.split("\n")], data[1:]))
    seen = [[[False] * 5 for i in range(5)] for j in range(len(boards))]

    winner = None

    played_sum = 0

    for next in bingo_stream:
        played_sum += next
        for x in range(0, len(boards)):
            if mark_square(boards[x], seen[x], next):
                winner = (boards[x], seen[x])
                break
        if winner is not None:
            break
    print(get_unmarked_sum(winner[0], winner[1]) * next)


def day4_part2():
    print(f"day4_part2")
    data = get_input()
    bingo_stream = list(map(lambda i: int(i), data[0].split(",")))

    boards = list(map(lambda p: [list(map(lambda b: int(b), list(filter(lambda z: z != "", y.split(" "))))) for y in p.split("\n")], data[1:]))
    seen = [[[False] * 5 for i in range(5)] for j in range(len(boards))]
    board_finished = [False] * len(boards)

    winner = None

    played_sum = 0

    for next in bingo_stream:
        played_sum += next
        for x in range(0, len(boards)):
            if not board_finished[x] and mark_square(boards[x], seen[x], next):
                winner = (boards[x], seen[x])
                board_finished[x] = True
        if all(board_finished):
            break

    print(get_unmarked_sum(winner[0], winner[1]) * next)


def mark_square(board, seen_board, number):
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == number:
                seen_board[i][j] = True
                if check_completion(seen_board):
                    return True

    return False


def check_completion(seen_board):
    for row in seen_board:
        if all(row):
            return True

    columns = zip(*[seen_board[i] for i in range(0, 5)])
    for col in columns:
        if all(col):
            return True

    return False


def get_unmarked_sum(board, seen):
    total = 0
    for i in range(5):
        for j in range(5):
            if seen[i][j] == False:
                total += board[i][j]

    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day4_part1()
    day4_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
