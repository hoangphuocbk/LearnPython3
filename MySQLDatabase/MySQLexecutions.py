#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql.cursors
import CreateNewDatabase

def insert(new_email, new_password):
	return "INSERT INTO users(email, password) values ('{0}', '{1}');".format(new_email, new_password)


if __name__ == '__main__':
	configs = CreateNewDatabase.readConfig("./install/MySQLConfig.txt")
	# connect to the database
	connection = pymysql.connect(host = 'localhost', user = configs['user'], password = configs['passwd'], db = "myDatabase")
	
	cursor = connection.cursor()
	
	# insert command
	sql = insert("youremail@gmail.com", "secret")
	print(sql)
	cursor.execute(sql)
	
	sql = insert("python@python.org", "very-secret")
	cursor.execute(sql)
	
	# query command
	sql = "SELECT id, password from users where email = %s ; "
	cursor.execute(sql,('webmaster@python.org',))
	result = cursor.fetchone()
	print(result)

	connection.commit()
	
	# close connection
	connection.close()
