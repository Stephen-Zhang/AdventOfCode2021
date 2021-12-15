import requests


def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/5/input', cookies=dict(session=cookie)).text[:-1]

    split_data = data.split("\n")

    processed_data = list(map(create_coordinates, split_data))

    return processed_data


def create_coordinates(row):
    (x, y) = row.split("->")
    x_coordinates = list(map(lambda a: int(a), x.strip().split(",")))
    y_coordinates = list(map(lambda a: int(a), y.strip().split(",")))

    return x_coordinates, y_coordinates


def is_ver(a):
    return a[0][0] == a[1][0]


def is_hor(a):
    return a[0][1] == a[1][1]


def is_diag(a):
    return abs(a[0][0] - a[1][0]) == abs(a[0][1] - a[1][1])


def day5_part1():
    print(f"day5_part1")
    data = get_input()

    filtered_data = list(filter(lambda a: is_hor(a) or is_ver(a), data))

    mp = {}

    dots = []

    for row in filtered_data:
        dots.extend(expand_line(row))

    for dot in dots:
        key = generate_key(dot)
        if key in mp:
            mp[key] += 1
        else:
            mp[key] = 1

    answer = list(filter(lambda x: mp[x] >= 2, mp.keys()))
    print(len(answer))


def day5_part2():
    print(f"day5_part2")
    data = get_input()

    filtered_data = list(filter(lambda a: is_hor(a) or is_ver(a) or is_diag(a), data))

    mp = {}

    dots = []

    for row in filtered_data:
        dots.extend(expand_line(row))

    for dot in dots:
        key = generate_key(dot)
        if key in mp:
            mp[key] += 1
        else:
            mp[key] = 1

    answer = list(filter(lambda x: mp[x] >= 2, mp.keys()))
    print(len(answer))


def expand_line(row):
    if is_hor(row):
        sorted_x = sorted([row[0][0], row[1][0]])
        return [(x, row[0][1]) for x in range(sorted_x[0], sorted_x[1] + 1)]
    elif is_ver(row):
        sorted_y = sorted([row[0][1], row[1][1]])
        return [(row[0][0], y) for y in range(sorted_y[0], sorted_y[1] + 1)]
    elif is_diag(row):
        sorted_row = sorted(row)
        increasing = sorted_row[0][1] < sorted_row[1][1]
        if increasing:
            return [(sorted_row[0][0] + a, sorted_row[0][1] + a) for a in range(sorted_row[1][0] - sorted_row[0][0] + 1)]
        else:
            return [(sorted_row[0][0] + a, sorted_row[0][1] - a) for a in range(sorted_row[1][0] - sorted_row[0][0] + 1)]
    else:
        return None


def generate_key(coordinate):
    # y*1000 + x
    return coordinate[1] * 1000 + coordinate[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day5_part1()
    day5_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
