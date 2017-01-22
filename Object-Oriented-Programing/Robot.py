#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class robot:
	''' Robot is represented with name '''
	population = 0
	def __init__(self, name):
		self.name = name
		# write host information when a new robot is created
		print("We are launching a new '{0}' robot".format(self.name))
		# when new robot was launched, population increase
		robot.population +=1

	def terminate(self):
		print("Terminating the {0} robot...".format(self.name))
		# decrease population of robots
		robot.population -= 1

		if robot.population == 0 :
			print("{0} robot was the last robot you had!".format(self.name))
		else:
			print("You still have {0} robots working!".format(robot.population))

	# define activity of robot
	def sayHello(self):
		print("Hello master, I'm {0}".format(self.name))
	
	@classmethod
	def howmany(ro):
		print("You have {0} robots".format(ro.population))

if __name__ == '__main__':
	r1 = robot("T2-micro")
	r2 = robot("C3-xlarge")
	r3 = robot("M5-large")
	
	# Robot r2 say hello to you
	r2.sayHello()

	# call Class method of robot class
	robot.howmany()

	# terminate r3
	r3.terminate()
	robot.howmany()
