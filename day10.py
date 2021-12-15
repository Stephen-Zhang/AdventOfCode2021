import requests
import math

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/10/input', cookies=dict(session=cookie)).text[:-1]

    # data = """
    # [({(<(())[]>[[{[]{<()<>>
    # [(()[<>])]({[<{<<[]>>(
    # (((({<>}<{<{<>}{[]{[]{}
    # {<[[]]>}<{[{[{[]{()[[[]
    # <{([{{}}[<[[[<>{}]]]>[]]
    # """.strip()

    return data.split("\n")


def day10_part1():
    print(f"day10_part1")
    data = get_input()

    points = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137,
        '' : 0
    }

    total = 0

    for row in data:
        value = solve_row(row)

        total += points[value]

    print(total)


def solve_row(row):
    stack = []
    for brace in row:
        if brace == '{' or brace == '[' or brace == '(' or brace == '<':
            stack.append(brace)
        elif brace == '}':
            if stack[-1] == '{':
                stack.pop(-1)
            else:
                return '}'
        elif brace == ']':
            if stack[-1] == '[':
                stack.pop(-1)
            else:
                return ']'
        elif brace == ')':
            if stack[-1] == '(':
                stack.pop(-1)
            else:
                return ')'
        elif brace == '>':
            if stack[-1] == '<':
                stack.pop(-1)
            else:
                return '>'
    return ''


def day10_part2():
    print(f"day10_part2")
    data = get_input()

    all_scores = list(filter(lambda x: x != -1, map(complete_row_score, data)))
    all_scores_sorted = sorted(all_scores)
    index = math.floor(len(all_scores_sorted) / 2)

    print(all_scores_sorted)
    print(all_scores_sorted[index])

def complete_row_score(row):
    stack = []
    for brace in row:
        if brace == '{' or brace == '[' or brace == '(' or brace == '<':
            stack.append(brace)
        elif brace == '}':
            if stack[-1] == '{':
                stack.pop(-1)
            else:
                return -1
        elif brace == ']':
            if stack[-1] == '[':
                stack.pop(-1)
            else:
                return -1
        elif brace == ')':
            if stack[-1] == '(':
                stack.pop(-1)
            else:
                return -1
        elif brace == '>':
            if stack[-1] == '<':
                stack.pop(-1)
            else:
                return -1

    scores = {
        '(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4
    }

    complete_score = 0
    while len(stack) > 0:
        last = stack.pop(-1)
        complete_score = complete_score * 5 + scores[last]

    return complete_score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day10_part1()
    day10_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
