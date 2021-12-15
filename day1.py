import requests

def getInput():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/1/input', cookies=dict(session=cookie)).text[:-1]

    split_data = data.split("\n")

    return split_data

def day1_part1():
    data = getInput()

    count = 0

    for row_num in range(1, len(data)):
        if int(data[row_num]) > int(data[row_num - 1]):
            print(f'{data[row_num]} is greater than {data[row_num - 1]}, count {count} increasing by 1...')
            count += 1

    print(f'increasing: {count} data: {data}')

def day1_part2():
    data = getInput()
    int_data = [int(x) for x in data]
    count = 0
    cleaned_data = [sum(int_data[x:x+3]) for x in range(0, len(data) - 2)]
    for row_num in range(1, len(cleaned_data)):
        if cleaned_data[row_num] > cleaned_data[row_num - 1]:
            count += 1

    print(f'increasing: {count} data: {data}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
