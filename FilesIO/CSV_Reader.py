#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

# open file 
newfile = open("SampleCSVFile.csv","r")
# read file
print("\n\nExample 1: Open file normally\n")
for line in newfile:
	clean_line = line.strip()
	print(clean_line)

# print some metadata
print("\n\nExample 2: Print metadata of the file\n")
print("Name of the file: ", newfile.name)
print("Opening mode: ", newfile.mode)
newfile.close()



# read file with the csv module
f = open("SampleCSVFile.csv","r")

print("\n\nExample 3: Read file with the CSV module")
csv_file = csv.reader(f, delimiter=',')
for line in csv_file:
	print(line)

f.close()
