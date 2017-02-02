#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def moving(h, source, destination, auxiliary):
	if h > 0:
		# move h - 1 disk from source to auxiliary
		moving(h-1, source, auxiliary, destination)
		# move largest disk from source to destination
		if(source[0]):
			moving_disk = source[0].pop()
			destination[0].append(moving_disk)
			print("Moving " + str(moving_disk) + " from " + source[1] + " to " + destination[1])
		# move h - 1 disk to destination 
		moving(h-1, auxiliary, destination, source)
		
if __name__ == '__main__':
	source = [[5,4,3,2,1], "source"]
	destination = [[], "destination"]
	auxiliary = [[], "auxiliary"]
	moving(5, source, destination, auxiliary)
