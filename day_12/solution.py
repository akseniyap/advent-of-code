data = []

with open('input.txt') as file:
    for line in file:
        data.append(line)

data = list(map(lambda x: x.strip(), data))
# print(data)

from collections import defaultdict
from os import pathsep

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.paths = []

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)


    def find_all_paths(self, vertex, destination):
        path = []
        visited = []

        self._find_all_paths(vertex, destination, path, visited)

    def _find_all_paths(self, vertex, destination, path, visited):
        path.append(vertex)
        if vertex.islower():
            visited.append(vertex)

        if vertex == destination:
            self.paths.append([*path])
        else:
            for adjacent in self.graph[vertex]:
                if adjacent not in visited:
                    self._find_all_paths(adjacent, destination, path, visited)

        path.pop()
        if vertex in visited:
            visited.remove(vertex)

    def find_all_paths_part2(self, vertex, destination):
        path = []
        visited = []
        can_duplicate = True

        self._find_all_paths_part2(vertex, destination, path, visited, can_duplicate)


    def _find_all_paths_part2(self, vertex, destination, path, visited, can_duplicate):
        path.append(vertex)
        if vertex.islower():
            visited.append(vertex)

        if vertex == destination:
            self.paths.append([*path])
        else:
            for adjacent in self.graph[vertex]:
                can_duplicate = set({i: visited.count(i) for i in visited}.values()) == {1}

                if adjacent not in visited:
                    self._find_all_paths_part2(adjacent, destination, path, visited, can_duplicate)
                elif adjacent in visited and adjacent != 'start' and can_duplicate:
                    self._find_all_paths_part2(adjacent, destination, path, visited, can_duplicate)

        path.pop()
        if vertex in visited:
            visited.remove(vertex)


def part_one(data):
    graph = Graph()
    for line in data:
        x, y = line.split('-')
        graph.add_edge(x, y)

    graph.find_all_paths('start', 'end')
    paths = graph.paths

    return len(paths)

print(part_one(data))


def part_two(data):
    graph = Graph()
    for line in data:
        x, y = line.split('-')
        graph.add_edge(x, y)

    graph.find_all_paths_part2('start', 'end')
    paths = graph.paths

    return len(paths)


print(part_two(data))
