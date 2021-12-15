import requests
import math

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/11/input', cookies=dict(session=cookie)).text[:-1]

#     data = """
# 5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526
#     """.strip()

    return data.split("\n")


def day11_part1():
    print(f"day11_part1")
    data = get_input()

    parsed_data = list(map(lambda row: [int(x) for x in row], data))

    total_flashes = 0

    for i in range(100):
        popped = []

        incremental_map(parsed_data)

        new_flashes = get_flashing(parsed_data, popped)
        while len(new_flashes) > 0:
            popped.extend(new_flashes)
            all_new_increments = [item for sublist in list(map(lambda coor: get_adj(coor[0], coor[1], len(data)), new_flashes)) for item in sublist]

            for incr in all_new_increments:
                parsed_data[incr[0]][incr[1]] += 1

            new_flashes = get_flashing(parsed_data, popped)

        total_flashes += len(popped)
        print(total_flashes)
        for coor in popped:
            parsed_data[coor[0]][coor[1]] = 0


def get_flashing(all, seen):
    all_coordinates = []
    for y in range(len(all)):
        for x in range(len(all[y])):
            if all[y][x] > 9 and (y, x) not in seen:
                all_coordinates.append((y, x))

    return all_coordinates


def incremental_map(all):
    for y in range(len(all)):
        for x in range(len(all[y])):
            all[y][x] += 1


def get_adj(y, x, size):
    all_points = [(y - 1, x - 1), (y, x - 1), (y + 1, x - 1),
            (y - 1, x), (y + 1, x),
            (y - 1, x + 1), (y, x + 1), (y + 1, x + 1)]

    filtered = list(filter(lambda coor: 0 <= coor[0] < size and 0 <= coor[1] < size, all_points))

    return filtered



def day11_part2():
    print(f"day11_part2")
    data = get_input()

    parsed_data = list(map(lambda row: [int(x) for x in row], data))

    total_flashes = 0

    for i in range(1, 1000):
        popped = []

        incremental_map(parsed_data)

        new_flashes = get_flashing(parsed_data, popped)
        while len(new_flashes) > 0:
            popped.extend(new_flashes)
            all_new_increments = [item for sublist in list(map(lambda coor: get_adj(coor[0], coor[1], len(data)), new_flashes)) for item in sublist]

            for incr in all_new_increments:
                parsed_data[incr[0]][incr[1]] += 1

            new_flashes = get_flashing(parsed_data, popped)

        if (len(popped) == 100):
            print(i)
            break

        for coor in popped:
            parsed_data[coor[0]][coor[1]] = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day11_part1()
    day11_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
