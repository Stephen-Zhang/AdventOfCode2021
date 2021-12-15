import requests
import math


def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/14/input', cookies=dict(session=cookie)).text[:-1]

#     data = """
# NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
#      """.strip()

    return data.split("\n")


def day14_part1():
    print(f"day14_part1")
    data = get_input()

    starter = data.pop(0)
    data.pop(0)
    rules = dict(map(generate_pair, data))

    next = starter
    for i in range(10):
        next = apply_transform(next, rules)

    counts = generate_count(next)

    inv_counts = {v: k for k, v in counts.items()}

    print(max(inv_counts.keys()) - min(inv_counts.keys()))


def generate_pair(row):
    (key, value) = row.split(" -> ")
    new_value = key[0] + value + key[1]

    return key, new_value


def apply_transform(starter, inputs):
    new_string = ''
    for x in range(len(starter) - 1):
        p = starter[x:x+2]
        if x == 0:
            new_string += inputs[p]
        else:
            new_string += inputs[p][1:]

    return new_string


def generate_count(string):
    letters = {}
    for i in string:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    return letters


def day14_part2():
    print(f"day14_part2")
    data = get_input()

    starter = data.pop(0)
    data.pop(0)
    rules = dict(map(generate_pair, data))

    starter_pairs = convert_starter_to_pairs(starter)

    all_pairs = starter_pairs
    for i in range(40):
        all_pairs = morph_pairs(all_pairs, rules)

        print(all_pairs)

    total_letters = count_letters(all_pairs)
    total_letters[starter[0]] += 1
    total_letters[starter[-1]] += 1

    reversed_letters = {v: k for k, v in total_letters.items()}
    print((max(reversed_letters.keys()) - min(reversed_letters.keys()))/2)


def convert_starter_to_pairs(string):
    pairs = {}

    for x in range(len(string) - 1):
        p = string[x:x+2]
        if p in pairs:
            pairs[p] += 1
        else:
            pairs[p] = 1

    return pairs

def morph_pairs(pairs, rules):
    new_pairs = {}

    for pair, count in pairs.items():
        generated_pairs = [rules[pair][0:2], rules[pair][1:]]
        for p in generated_pairs:
            if p in new_pairs:
                new_pairs[p] += count
            else:
                new_pairs[p] = count

    return new_pairs


def count_letters(pairs):
    letters = {}
    for pair, count in pairs.items():
        for i in pair:
            if i in letters:
                letters[i] += count
            else:
                letters[i] = count
    return letters

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day14_part1()
    day14_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
