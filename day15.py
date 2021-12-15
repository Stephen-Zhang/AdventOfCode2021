import requests
import cProfile
import pstats
from pstats import SortKey

pr = cProfile.Profile()

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/15/input', cookies=dict(session=cookie)).text[:-1]

    data = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
         """.strip()

    return data.split("\n")


class Node:
    def __init__(self, parent, pos, cost):
        self.parent = parent
        self.pos = pos
        self.cost = cost

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self):
        return f"{self.pos}, f: {self.f}"


def get_path_cost(node):
    current = node
    cost = 0
    while current is not None:
        cost += current.cost
        current = current.parent
    return cost


def day15_part1():
    print(f"day15_part1")
    data = get_input()

    d_pts = list(map(lambda row: [int(x) for x in row], data))

    cost = solve_path(d_pts)

    print(cost)


def solve_path(d_pts):
    max_x = len(d_pts[0]) - 1
    max_y = len(d_pts) - 1
    start = (0, 0)
    end = (max_x, max_y)
    start_node = Node(None, start, 0)
    end_node = Node(None, end, get_cost(end, d_pts))

    stack = [start_node]
    explored = []

    while len(stack) > 0:
        curr_node = stack.pop(0)
        explored.append(curr_node)

        if curr_node == end_node:
            return get_path_cost(curr_node)

        need_sort = False

        neighbors = get_adj(curr_node.pos, max_x, max_y)
        for neighbor in neighbors:
            n_node = Node(curr_node, neighbor, get_cost(neighbor, d_pts))
            if n_node in explored:
                continue

            n_node.g = curr_node.g + n_node.cost
            n_node.h = manhattan_dist(n_node.pos, end_node.pos)
            n_node.f = n_node.g + n_node.h

            if n_node in stack:
                ind = stack.index(n_node)
                if n_node.g < stack[ind].g:
                    stack[ind] = n_node
                    need_sort = True
            else:
                stack.append(n_node)
                need_sort = True
        if need_sort:
            stack.sort(key=lambda x: x.f)


def get_cost(pt, data):
    return data[pt[1]][pt[0]]


def manhattan_dist(c, end):
    return abs(c[0] - end[0]) + abs(c[1] - end[1])


def get_adj(c, sizeX, sizeY):
    (x, y) = c
    adj = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    filtered_adj = list(filter(lambda c: 0 <= c[0] <= sizeX and 0 <= c[1] <= sizeY, adj))
    return filtered_adj


def day15_part2():
    pr.enable()
    print(f"day15_part2")
    data = get_input()

    d_pts = list(map(lambda row: [int(x) for x in row], data))

    new_d_pts = generate_new_data(d_pts)

    cost = solve_path(new_d_pts)
    print(cost)

    pr.disable()
    pr.print_stats(sort=SortKey.CUMULATIVE)


def generate_new_data(d_pts):
    new_map = [[] for _ in range(5)]
    for i in range(0, 5):
        for j in range(0, 5):
            new_map[j].append(increase_data(i+j, d_pts))

    combined_cube = []
    for big_row in new_map:
        combined_row = [[] for _ in range(len(d_pts[0]))]
        for square in big_row:
            for ind, y in enumerate(square):
                combined_row[ind].extend(y)
        combined_cube.append(combined_row)

    flattened_cube = [x for sublist in combined_cube for x in sublist]

    return flattened_cube


def increase_data(total_increase, pts):
    return list(map(lambda x: [((y + total_increase - 1) % 9) + 1 for y in x], pts))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day15_part1()
    day15_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
