import requests
import statistics
import math

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/7/input', cookies=dict(session=cookie)).text[:-1]

    return data


def day7_part1():
    print(f"day7_part1")
    data = get_input()

    num_data = list(map(lambda x: int(x), data.split(",")))
    median = statistics.median(num_data)

    dist_traveled = [abs(x - median) for x in num_data]

    print(median)
    print(dist_traveled)
    print(sum(dist_traveled))


def day7_part2():
    print(f"day7_part2")
    data = get_input()

    num_data = list(map(lambda x: int(x), data.split(",")))

    dists = []

    for m in range(min(num_data), max(num_data) + 1):
        dist_traveled = [math.ceil((abs(x - m) * (abs(x - m) + 1)) / 2) for x in num_data]

        dists.append(sum(dist_traveled))

    print(dists)
    print(min(dists))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day7_part1()
    day7_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
