#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import os
import csv

# open the existed file
f = open('SampleCSVFile.csv','r')
# set name for the new file
newfile = 'NewCSVFile'

# check if the new file's already existed
if(os.path.exists(newfile)):
	print("Delete file ", newfile)
	os.remove(newfile)	# delete file

# read content from file to newfile
wf = open(newfile,'w')

reader = csv.reader(f)
writer = csv.writer(wf, delimiter = '\t')

for line in reader:
	writer.writerow(line)

f.close()
wf.close()
