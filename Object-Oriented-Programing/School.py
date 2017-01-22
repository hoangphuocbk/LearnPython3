#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	# define tell activity
	def tell(self):
		print("Hi all, I'm {0} and a {1}.".format(self.name, self.__class__.__name__), end = " ")

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
	def tell(self):
		SchoolMember.tell(self)
		print("My salary is {0} $ per month!".format(self.salary))

class Student(SchoolMember):
	def __init__(self, name, age, mark):
		SchoolMember.__init__(self, name, age)
		self.mark = mark
	def tell(self):
		SchoolMember.tell(self)
		print("My mark is {0}.".format(self.mark))

if __name__ == '__main__':
	t1 = Teacher("Thao", 25, 20000)
	s1 = Student("Joshual", 21, 10)

	t1.tell()
	s1.tell()
