import requests
import math


def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/13/input', cookies=dict(session=cookie)).text[:-1]

#     data = """
# 6, 10
# 0, 14
# 9, 10
# 0, 3
# 10, 4
# 4, 11
# 6, 0
# 6, 12
# 4, 1
# 0, 13
# 10, 12
# 3, 4
# 3, 0
# 8, 4
# 1, 10
# 2, 14
# 8, 10
# 9, 0
#
# fold along y=7
# fold along x=5
#      """.strip()

    return list(map(lambda list: list.split("\n"), data.split("\n\n")))


def day13_part1():
    print(f"day13_part1")
    data = get_input()

    dots = list(map(lambda x: (int(x[0]), int(x[1])), [y.split(",") for y in data[0]]))

    fold = data[1][0].replace("fold along ", "")
    fold = fold.split("=")
    if fold[0] == 'x':
        fold_line = (int(fold[1]), 0)
    elif fold[0] == 'y':
        fold_line = (0, int(fold[1]))

    prefold_dots = list(filter(lambda dot: dot[0] >= fold_line[0] and dot[1] >= fold_line[1], dots))
    static_dots = [x for x in dots if x not in prefold_dots]

    folded_dots = reflect_line(fold_line, prefold_dots)

    all_dots = set()
    all_dots.update(static_dots)
    all_dots.update(folded_dots)

    print(len(all_dots))


def reflect_line(line, prefold_dots):
    if line[0] == 0:
        # horizontal line flip
        folded_dots = list(map(lambda dot: (dot[0], 2*line[1] - dot[1]), prefold_dots))

    elif line[1] == 0:
        # vertical line flip
        folded_dots = list(map(lambda dot: (2*line[0] - dot[0], dot[1]), prefold_dots))

    return folded_dots

def day13_part2():
    print(f"day13_part2")
    data = get_input()

    dots = list(map(lambda x: (int(x[0]), int(x[1])), [y.split(",") for y in data[0]]))

    folds = list(map(parse_fold, data[1]))

    folded_dots = set(dots)
    for fold in folds:
        prefold_dots = list(filter(lambda dot: dot[0] >= fold[0] and dot[1] >= fold[1], folded_dots))
        static_dots = [x for x in folded_dots if x not in prefold_dots]

        new_dots = reflect_line(fold, prefold_dots)
        folded_dots = set(new_dots)
        folded_dots.update(static_dots)

    print_map(folded_dots)




def parse_fold(row):
    fold = row.replace("fold along ", "")
    fold = fold.split("=")
    if fold[0] == 'x':
        fold_line = (int(fold[1]), 0)
    elif fold[0] == 'y':
        fold_line = (0, int(fold[1]))

    return fold_line


def print_map(dots):
    max_x = max([x[0] for x in dots])
    max_y = max([x[1] for x in dots])

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in dots:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print('\n', end='')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day13_part1()
    day13_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
