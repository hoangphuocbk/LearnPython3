#!/usr/bin/env python3
# -*- coding: utf-8 -*-

graph = {
	"a": ["c"],
	"b": ["c", "e"],
	"c": ["a", "b", "d", "e"],
	"d": ["c"],
	"e": ["b", "c"],
	"f": []
}

def generate_edges(graph):
	edges = []
	for node in graph:
		for neighbour in graph[node]:
			edges.append((node, neighbour))
	return edges

def find_isolated_nodes(graph):
	isolated = []
	for node in graph:
		if not graph[node]:
			isolated += node
	return isolated

if __name__ == '__main__':
	print(generate_edges(graph))
	print(find_isolated_nodes(graph))
