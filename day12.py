import requests
import copy

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/12/input', cookies=dict(session=cookie)).text[:-1]

#     data = """
# fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW
#      """.strip()

    return data.split("\n")


class Node:
    def __init__(self, name, is_big, special_small = False):
        self.name = name
        self.big = is_big
        self.neighbors = []
        self.special_small = special_small

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_neighbors(self):
        return self.neighbors


def day12_part1():
    print(f"day12_part1")
    data = get_input()

    nodes = {}

    for row in data:
        (name, neighbor) = row.split("-")

        if name not in nodes:
            big = name.isupper()
            nodes[name] = Node(name, big)
        if neighbor not in nodes:
            big = neighbor.isupper()
            nodes[neighbor] = Node(neighbor, big)
        nodes[name].add_neighbor(neighbor)
        nodes[neighbor].add_neighbor(name)

    paths = generate_paths(nodes['start'], nodes['end'], nodes, [])

    print(len(paths))


def generate_paths(current, end, all_nodes, visited):
    visited.append(current)

    if current == end:
        return [','.join(list(map(lambda node: node.name, visited)))]

    paths = []
    for neighbor in current.neighbors:
        if all_nodes[neighbor].big or all_nodes[neighbor] not in visited:
            paths.append(generate_paths(all_nodes[neighbor], end, all_nodes, visited.copy()))

    paths = [x for sublist in paths for x in sublist]

    return paths


def day12_part2():
    print(f"day12_part2")
    data = get_input()

    nodes = {}

    for row in data:
        (name, neighbor) = row.split("-")

        if name not in nodes:
            big = name.isupper()
            nodes[name] = Node(name, big)
        if neighbor not in nodes:
            big = neighbor.isupper()
            nodes[neighbor] = Node(neighbor, big)
        nodes[name].add_neighbor(neighbor)
        nodes[neighbor].add_neighbor(name)

    all_special_node_sets = []

    for node in nodes:
        if node != 'start' and node != 'end' and not node.isupper():
            new_node_set = copy.deepcopy(nodes)
            new_node_set[node].special_small = True
            all_special_node_sets.append(new_node_set)

    all_paths = set()
    for node_set in all_special_node_sets:
        paths = generate_paths_modified(node_set['start'], node_set['end'], node_set, [])
        all_paths.update(paths)

    print(len(all_paths))


def generate_paths_modified(current, end, all_nodes, visited):
    visited.append(current)

    if current == end:
        return [','.join(list(map(lambda node: node.name, visited)))]

    paths = []
    for neighbor in current.neighbors:
        if all_nodes[neighbor].big or (all_nodes[neighbor].special_small and visited.count(all_nodes[neighbor]) == 1) or all_nodes[neighbor] not in visited:
            paths.append(generate_paths_modified(all_nodes[neighbor], end, all_nodes, visited.copy()))

    paths = [x for sublist in paths for x in sublist]

    return paths

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day12_part1()
    day12_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
