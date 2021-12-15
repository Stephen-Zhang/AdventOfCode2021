import requests


def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/3/input', cookies=dict(session=cookie)).text[:-1]

    split_data = data.split("\n")

    return split_data


def day3_part1():
    print(f"day3_part1")
    data = get_input()

    cleaned_data = []
    for y in range(len(data[0])):
        cleaned_data.append([])
        for x in range(len(data)):
            cleaned_data[y] += data[x][y]

    gamma = ""
    epsilon = ""

    for row in cleaned_data:
        if row.count('1') > len(data) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            epsilon += '1'
            gamma += '0'

    print(f'gamma: {gamma} epsilon: {epsilon}')

    print(int(gamma, 2) * int(epsilon, 2))


def day3_part2():
    print(f"day3_part2")
    data = get_input()

    oxygen = calculate_oxygen(data, 0)
    co2 = calculate_co2(data, 0)

    print(f'oxygen: {oxygen}, co2: {co2}')

    print(int(co2, 2) * int(oxygen, 2))


def calculate_oxygen(data, index):
    if index > len(data[0]):
        print("SOMETHING WENT WRONG")
        return -1
    if len(data) == 1:
        return data[0]

    majority = get_majority_bit(data, index)
    return calculate_oxygen(filter_by_index(data, majority, index), index + 1)


def calculate_co2(data, index):
    if index > len(data[0]):
        print("SOMETHING WENT WRONG")
        return -1
    if len(data) == 1:
        return data[0]

    majority = get_majority_bit(data, index)

    minority = '1' if majority == '0' else '0'
    return calculate_co2(filter_by_index(data, minority, index), index + 1)


def get_majority_bit(iterable, index):
    ones = 0
    for x in iterable:
        if x[index] == '1':
            ones += 1

    return '1' if ones >= len(iterable) / 2 else '0'


def filter_by_index(iterable, bit, index):
    out = list(filter(lambda x: x[index] == bit, iterable))
    return out


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day3_part1()
    day3_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
