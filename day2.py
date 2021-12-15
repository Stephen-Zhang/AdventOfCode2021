import requests

def getInput():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/2/input', cookies=dict(session=cookie)).text[:-1]

    split_data = data.split("\n")

    return split_data

def day2_part1():
    data = getInput()

    split_data = [x.split(' ') for x in data]
    horizontal = [x for x in split_data if x[0] == 'forward']
    down = [x for x in split_data if x[0] == 'down']
    up = [x for x in split_data if x[0] == 'up']

    horizontal_sum = sum([int(x[1]) for x in horizontal])
    down_sum = sum([int(x[1]) for x in down])
    up_sum = sum([int(x[1]) for x in up])

    print(f'horizontal: {horizontal_sum}, down: {down_sum}, up: {up_sum}')
    print(horizontal_sum * (down_sum - up_sum))


def day2_part2():
    data = getInput()
    split_data = [x.split(' ') for x in data]
    depth = 0
    horizontal = 0
    aim = 0

    for move in split_data:
        dist = int(move[1])
        if move[0] == 'forward':
            horizontal += dist
            depth += dist * aim
        elif move[0] == 'down':
            aim += dist
        elif move[0] == 'up':
            aim -= dist
        print(f'horizontal: {horizontal}, depth: {depth}, aim: {aim}')

    print(horizontal * depth)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day2_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
