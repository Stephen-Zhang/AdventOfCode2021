import requests
import math

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/9/input', cookies=dict(session=cookie)).text[:-1]

#     data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""

    return data.split("\n")


def day9_part1():
    print(f"day9_part1")
    data = get_input()

    map_of_lava = [[int(x) for x in row] for row in data]

    total = 0

    for x in range(len(map_of_lava[0])):
        for y in range(len(map_of_lava)):
            if is_low_point(x, y, map_of_lava):
                total += map_of_lava[y][x] + 1

    print(total)


def is_low_point(x, y, arr):
    points_to_check = get_valid_points(x, y, arr)

    is_low_point = True

    for pt in points_to_check:
        if (arr[y][x] >= arr[pt[1]][pt[0]]):
            is_low_point = False
            break

    return is_low_point


def get_valid_points(x, y, lava_map):
    left = (x - 1, y)
    right = (x + 1, y)
    up = (x, y - 1)
    down = (x, y + 1)

    valid_points = [left, right, up, down]

    valid_points = list(filter(lambda pt: pt[0] >= 0 and pt[0] < len(lava_map[0]) and pt[1] >= 0 and pt[1] < len(lava_map), valid_points))

    return valid_points


def day9_part2():
    print(f"day9_part2")
    data = get_input()
    lava_map = [[int(x) for x in row] for row in data]

    all_coordinates = [(x, y) for x in range(len(lava_map[0])) for y in range(len(lava_map))]
    all_unsorted_coordinates = list(filter(lambda pt: lava_map[pt[1]][pt[0]] != 9, all_coordinates))

    basins = []

    while len(all_unsorted_coordinates) != 0:
        basin = []

        c = all_unsorted_coordinates.pop()
        coordinates_to_check = [c]

        while len(coordinates_to_check) != 0:
            next = coordinates_to_check.pop()
            basin.append(next)

            adj_c = get_valid_points(next[0], next[1], lava_map)
            for adj in adj_c:
                if adj in all_unsorted_coordinates:
                    all_unsorted_coordinates.remove(adj)
                    coordinates_to_check.append(adj)

        basins.append(basin)

    basin_sizes = [len(x) for x in basins]
    biggest_basin_sizes = sorted(basin_sizes)[-3:]

    print(biggest_basin_sizes)
    print(math.prod(biggest_basin_sizes))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day9_part1()
    day9_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
