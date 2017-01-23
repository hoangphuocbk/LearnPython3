#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

while True:
	try:
		# reading from sys.stdin (stop Ctrl-D)
		number = input("Enter a number: ")
		# output to stdout
		# print("Processing {0} number".format(number))
	except EOFError:
		print("ciao")
		break
	else:
		number = int(number)
		print(number)
		if number == 0:
			print("0 has no inverse", file=sys.stderr)
		else:
			print("Inverse of {0} is {1}".format(number,1/number))
