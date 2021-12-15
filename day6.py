import requests


def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/6/input', cookies=dict(session=cookie)).text[:-1]

    split_data = data.split("\n")

    return split_data

RESET_FISH = 6
NEW_FISH = 8


def day6_part1():
    print(f"day6_part1")
    data = get_input()

    fish = list(map(lambda x: int(x), data[0].split(",")))

    count = [fish.count(x) for x in range(0, 9)]

    for i in range(80):
        new_fish = count[0]
        count = count[1:]
        count.append(new_fish)
        count[6] += new_fish

    print(sum(count))


def day6_part2():
    print(f"day6_part2")
    data = get_input()

    fish = list(map(lambda x: int(x), data[0].split(",")))

    count = [fish.count(x) for x in range(0, 9)]

    for i in range(256):
        new_fish = count[0]
        count = count[1:]
        count.append(new_fish)
        count[6] += new_fish

    print(sum(count))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day6_part1()
    day6_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
