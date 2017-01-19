#!/usr/bin/env python3
# -*- coding: utf-8 -*-

your_str = input("Write your new sentence in there: ")

your_list = your_str.split()

# print list
print(your_list)

# loop each element by using for
for i in your_list:
	print(i)

print("Done\n\n")
print("############################################")

SUFFIXS = {
	1000: ['KB', 'MB', 'GB', 'TB', 'PB'],
	1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
}

size = int(input("Put your HDD size in here: "))
typeHDD = int(input("What is your unit, 1000(B) or 1024(iB)? "))

value = size
index = ''
for i in SUFFIXS[typeHDD]:
	value = value/typeHDD
	if( value > typeHDD):
		pass
	else:
		index = i
		break

print("Your HDD size: %1.3f %s" %(value, index))
