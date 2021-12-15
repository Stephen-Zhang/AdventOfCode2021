import requests
import statistics
import math

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/8/input', cookies=dict(session=cookie)).text[:-1]

    return data.split("\n")


def day8_part1():
    print(f"day8_part1")
    data = get_input()

    parsed_data = [y.split("|") for y in data]
    parsed_data = list(map(lambda x: (x[0].strip().split(" "), x[1].strip().split(" ")), parsed_data))

    total = 0
    for row in parsed_data:
        output_values = row[1]
        total += len(list(filter(lambda x: len(x) == 2, output_values)))  # 1 digit
        total += len(list(filter(lambda x: len(x) == 4, output_values)))  # 4 digit
        total += len(list(filter(lambda x: len(x) == 3, output_values)))  # 7 digit
        total += len(list(filter(lambda x: len(x) == 7, output_values)))  # 8 digit

    print(total)


def day8_part2():
    print(f"day8_part2")
    data = get_input()

    parsed_data = [y.split("|") for y in data]
    parsed_data = list(map(lambda x: (x[0].strip().split(" "), x[1].strip().split(" ")), parsed_data))

    convert_to_array(parsed_data[0][0][0])


    # KNOWN 1 4 7 8
    # -- 6 DIGITS
    # 6 if it DOES NOT have 1 in it
    # 0 if it DOES NOT CONTAINS DIFF(1+4)
    # 9 if it DOES CONTAIN DIFF(1+4)
    # -- 5 DIGITS
    # 5 if it DOES CONTAIN DIFF(1+4)
    # 2 if it DOES NOT CONTAIN 1
    # 3 if it DOES CONTAIN 1

    total = 0
    for row in parsed_data:
        (dv, ov) = row
        dva = list(map(convert_to_array, dv))
        solved = solve_puzzle(dva)

        inv_solved = {array_to_key(v): k for k, v in solved.items()}
        ova = list(map(lambda x: array_to_key(convert_to_array(x)), ov))

        total += int(''.join([f"{inv_solved[x]}" for x in ova]))

    print(total)


def solve_puzzle(dva):
    solved = {}
    solved[1] = next(filter(lambda x: sum(x) == 2, dva))
    solved[4] = next(filter(lambda x: sum(x) == 4, dva))
    solved[7] = next(filter(lambda x: sum(x) == 3, dva))
    solved[8] = next(filter(lambda x: sum(x) == 7, dva))
    solved[6] = next(filter(lambda x: sum(x) == 6 and solved[1] != and_lists(solved[1], x), dva))
    solved[0] = next(filter(lambda x: sum(x) == 6 and (solved[1] == and_lists(solved[1], x) and (
                xor_lists(solved[1], solved[4]) != and_lists(xor_lists(solved[1], solved[4]), x))), dva))
    solved[9] = next(filter(lambda x: sum(x) == 6 and (solved[1] == and_lists(solved[1], x) and (
                xor_lists(solved[1], solved[4]) == and_lists(xor_lists(solved[1], solved[4]), x))), dva))
    solved[5] = next(filter(
        lambda x: sum(x) == 5 and xor_lists(solved[1], solved[4]) == and_lists(xor_lists(solved[1], solved[4]), x),
        dva))
    solved[2] = next(filter(lambda x: sum(x) == 5 and (
                xor_lists(solved[1], solved[4]) != and_lists(xor_lists(solved[1], solved[4]), x)) and (
                                                  solved[1] != and_lists(solved[1], x)), dva))
    solved[3] = next(filter(lambda x: sum(x) == 5 and (
                xor_lists(solved[1], solved[4]) != and_lists(xor_lists(solved[1], solved[4]), x)) and (
                                                  solved[1] == and_lists(solved[1], x)), dva))

    return solved


def convert_to_array(input_str):
    output = [False] * 8
    for x in input_str:
        value = ord(x) - ord('a')
        output[value] = True
    return output


def array_to_key(arr):
    return ''.join(['0' if x else '1' for x in arr])



def and_lists(listA, listB):
    return [a and b for a, b in zip(listA, listB)]


def xor_lists(listA, listB):
    return [(a and not b) or (b and not a) for a,b in zip(listA, listB)]


def or_lists(listA, listB):
    return [a or b for a, b in zip(listA, listB)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day8_part1()
    day8_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
