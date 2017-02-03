#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# return quantity * price each item if it is large than 100 else add up to 10
calculatePrice = lambda x: (x[0], x[2]*x[3]) if x[2]*x[3] > 100 else (x[0], x[2]*x[3] + 10)

if __name__ == '__main__':
	# input values
	orders = [
		["34587", "Learning Python, Mark Lutz", 4, 40.95],
		["98762", "Programming Python, Mark Lutz", 5, 56.80],
		["77226", "Head First Python, Paul Barry", 3, 32.95],
		["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
	]
	# output is list of 2-tuple with order number and price after calculating
	price = list(map(calculatePrice, orders))
	# print out the result
	print(price)
