#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Graph:
	# initial graph
	def __init__(self, graph_dict = None):
		if graph_dict == None:
			graph_dict = {}
		self.__graph_dict = graph_dict
	
	# add new vertex
	def add_vertex(vertex):
		if vertex in self.__graph_dict:
			pass
		else:
			self.__graph_dict[vertex] = []
	
	# add new edge
	def add_edge(self, *edge):
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		flag = True

		# add neighbour for vertex1
		if vertex1 in self.__graph_dict:
			if vertex2 not in self.__graph_dict[vertex1]:
				self.__graph_dict[vertex1].append(vertex2)
			else:
				flag = False
		else:
			self.__graph_dict[vertex1] = [vertex2]
		# add neighbour for vertex2
		if vertex2 in self.__graph_dict:
			if vertex1 not in self.__graph_dict[vertex2]:
				self.__graph_dict[vertex2].append(vertex1)
		else:
			self.__graph_dict[vertex2] = [vertex1]

	# get vertices
	def get_vertices(self):
		return list(self.__graph_dict.keys())

	# generate edge
	def generate_edge(self):
		edges = []
		for node in self.__graph_dict:
			for neighbour in self.__graph_dict[node]:
				if ((node, neighbour) not in edges) and ((neighbour, node) not in edges):
					edges.append((node, neighbour))
		return edges

	# get edges
	def get_edges(self):
		return self.generate_edge()

	# overwrite print method
	def __str__(self):
		str = "{\n"
		for node in self.__graph_dict:
			str = str + "\"" + node + "\": ["
			for neighbour in self.__graph_dict[node]:
				str = str +  "\"" + neighbour + "\", "
			str = str + "]\n"
		str = str + "\n}"
		return str

if __name__ == '__main__':
	graph = {
    "a": ["c"],
    "b": ["c", "e"],
    "c": ["a", "b", "d", "e"],
    "d": ["c"],
    "e": ["b", "c"],
    "f": []
	}
	
	g = Graph(graph)
	print(g.get_vertices())
	print(g.get_edges())
	# print(g)
	print("############ add new edge a - f ############")
	g.add_edge("a" , "f")
	print("############ add new edge x - y ############")
	g.add_edge("x" , "y")
	print(g)
