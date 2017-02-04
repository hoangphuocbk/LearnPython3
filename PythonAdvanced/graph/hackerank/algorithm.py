#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# initiate graph dict from file
def graph(filename):
    n_graph = {}
    with open( filename ) as f:
        N = f.readline().rstrip('\n')
        for line in f.readlines():
            line = line.rstrip('\n')
            edge = line.split(',')
            # print('{0}   -   {1}'.format(edge[0], edge[1]))
            if edge[0] in n_graph:
                n_graph[edge[0]].append(edge[1])
            else:
                n_graph[edge[0]] = [edge[1]]
            if edge[1] in n_graph:
                n_graph[edge[1]].append(edge[0])
            else:
                n_graph[edge[1]] = [edge[0]]
    return n_graph

# caculate distance on graph
def findPath(n_graph, first, last, path = []):

    path = path + [first]

    if first == last:
        return path

    if first not in n_graph:
        return None

    for neighbour in n_graph[first]:
        if neighbour not in path:
            extened_path = findPath(n_graph, neighbour, last, path)
            if extened_path:
                return extened_path
    return None

if __name__ == '__main__':
    n_graph = graph('training.txt')
    # print(n_graph)
    print(len(findPath(n_graph, '4', '5')))
