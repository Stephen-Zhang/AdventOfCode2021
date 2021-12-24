import sys

import requests
import heapq as hq

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/17/input', cookies=dict(session=cookie)).text[:-1]

#     data = """
# target area: x=20..30, y=-10..-5
#          """.strip()

    return data


def day17_part1():
    print(f"day17_part1")
    data = get_input()

    min_x, max_x, min_y, max_y = parse_data(data)

    curr_y = 0
    for x in range(max_x * 2):
        for y in range(min_y, 200):
            hit, positions = test_shot(x, y, min_x, max_x, min_y, max_y)
            if hit and y > curr_y:
                curr_y = y
                result = max([p[1] for p in positions])
                print(f"Hit at y: {curr_y}, result:{result}")

    # draw_board(positions, min_x, max_x, min_y, max_y)


def test_shot(x, y, min_x, max_x, min_y, max_y):
    # ADJUST THESE
    x_vel, y_vel = (x, y)

    positions = []
    probe_x, probe_y = (0, 0)

    max_steps = 1000
    counter = 0
    hit = False
    while counter < max_steps:
        counter += 1
        probe_x += x_vel
        probe_y += y_vel

        positions.append((probe_x, probe_y))

        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1

        y_vel -= 1

        if (probe_x > max_x or probe_y < min_y):
            break
        elif (min_x <= probe_x <= max_x and min_y <= probe_y <= max_y):
            hit = True
            break

    return hit, positions


def draw_board(probe_pos, min_x_target, max_x_target, min_y_target, max_y_target):
    max_y_board = max([p[1] for p in probe_pos])

    plot_probe_pos = [(0, 0)] + probe_pos
    plot_probe_pos = list(map(lambda p: (p[0], p[1] - max_y_board), plot_probe_pos))

    board_x = max_x_target + 1
    board_y = max_y_board - min_y_target + 1

    for y in range(board_y):
        for x in range(board_x):
            if (x, -y) in plot_probe_pos:
                if (x == 0):
                    print("S", end='')
                else:
                    print("#", end='')
            elif min_x_target <= x <= max_x_target and min_y_target <= -(y - max_y_board) <= max_y_target:
                print("T", end='')
            else:
                print('.', end='')
        print()

def day17_part2():
    print(f"day17_part2")
    data = get_input()

    min_x, max_x, min_y, max_y = parse_data(data)

    count = 0
    for x in range(max_x * 2):
        for y in range(min_y, 200):
            hit, positions = test_shot(x, y, min_x, max_x, min_y, max_y)
            if hit:
                count += 1
                print(f"Hit at x:{x} y: {y}, count: {count}")

    print(f"final count: {count}")

def parse_data(data):
    cleaned = data.replace("target area: ", "")
    x_split, y_split = cleaned.split(", ")
    x_split = x_split.replace("x=", "")
    min_x, max_x = x_split.split("..")
    y_split = y_split.replace("y=", "")
    min_y, max_y = y_split.split("..")

    return int(min_x), int(max_x), int(min_y), int(max_y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day17_part1()
    day17_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
