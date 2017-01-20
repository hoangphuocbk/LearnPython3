#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import os
import csv

# open the existed file
f = open('SampleCSVFile.csv','r')
# set name for the new file
newfile = 'NewCSVFile.csv'

# check if the new file's already existed
if(os.path.exists(newfile)):
	print("Delete file ", newfile)
	os.remove(newfile)	# delete file

# read content from file to newfile
wf = open(newfile,'w')

reader = csv.reader(f)
writer = csv.writer(wf, delimiter=',')

# eliminate column 1 that is not necessary
for line in reader:
	newline = line[1:]
	writer.writerow(newline)

# close all files
f.close()
wf.close()
