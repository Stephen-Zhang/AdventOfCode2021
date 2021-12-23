import requests
import heapq as hq

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/15/input', cookies=dict(session=cookie)).text[:-1]

#     data = """
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581
#          """.strip()

    return data.split("\n")


class Node:
    def __init__(self, parent, pos, cost):
        self.parent = parent
        self.pos = pos
        self.cost = cost

        self.g = 0
        self.h = 0
        self.f = 0

    def __gt__(self, other):
        return self.f > other.f

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self):
        return f"{self.pos}, f: {self.f}"

def index(pos, maxY):
    return pos[1] * maxY + pos[0]


def get_path_cost(node):
    current = node
    cost = 0
    while current is not None:
        print(f"{current.pos}", end=" <- ")
        cost += current.cost
        current = current.parent
    print()
    return cost


def day15_part1():
    print(f"day15_part1")
    data = get_input()

    d_pts = list(map(lambda row: [int(x) for x in row], data))

    cost = solve_path(d_pts)

    print(cost)


def solve_path(d_pts):
    max_x = len(d_pts[0])
    max_y = len(d_pts)
    start = (0, 0)
    end = (max_x - 1, max_y - 1)
    start_node = Node(None, start, 0)
    end_node = Node(None, end, get_cost(end, d_pts))

    stack = [start_node]
    hq.heapify(stack)
    explored = [False for x in range(len(d_pts)*len(d_pts))]

    while len(stack) > 0:
        curr_node = hq.heappop(stack)
        i = index(curr_node.pos, max_y)
        if explored[i]:
            continue
        explored[i] = True

        if curr_node == end_node:
            return get_path_cost(curr_node)

        neighbors = get_adj(curr_node.pos, max_x, max_y)
        for neighbor in neighbors:
            n_node = Node(curr_node, neighbor, get_cost(neighbor, d_pts))
            if explored[index(n_node.pos, max_y)]:
                continue

            n_node.g = curr_node.g + n_node.cost
            n_node.h = manhattan_dist(n_node.pos, end_node.pos)
            n_node.f = n_node.g + n_node.h

            hq.heappush(stack, n_node)


def get_cost(pt, data):
    return data[pt[1]][pt[0]]


def manhattan_dist(c, end):
    return abs(c[0] - end[0]) + abs(c[1] - end[1])


def get_adj(c, sizeX, sizeY):
    (x, y) = c
    adj = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    filtered_adj = list(filter(lambda c: 0 <= c[0] < sizeX and 0 <= c[1] < sizeY, adj))
    return filtered_adj


def day15_part2():
    print(f"day15_part2")
    data = get_input()

    d_pts = list(map(lambda row: [int(x) for x in row], data))

    new_d_pts = generate_new_data(d_pts)

    cost = solve_path(new_d_pts)
    print(cost)


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
