#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# The first example

''' 
your_str = input("Write your new sentence in there: ")

your_list = your_str.split()

# print list
print(your_list)

# loop each element by using for
for i in your_list:
	print(i)
'''


print("Done\n\n")
print("############################################")

SUFFIXS = {
	1000: ['KB', 'MB', 'GB', 'TB', 'PB'],
	1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
}

try:
	size = int(input("Put your HDD size in here: "))
except ValueError:
	print("You put the size number that is not number")

try:
	typeHDD = int(input("What is your unit, 1000(B) or 1024(iB)? "))
	if((typeHDD != 1000) and (typeHDD != 1024)):
		sys.exit("Error type of your HDD")
except ValueError:
	print("You put type of HDD that is not number")

value = size
index = ''
for i in SUFFIXS[typeHDD]:
	value = value/typeHDD
	if( value >= typeHDD):
		pass
	else:
		index = i
		break

print("Your HDD size: %1.1f %s" %(value, index))
