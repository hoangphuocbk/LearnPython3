#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import time

def sleep(name, i):
	print("Thread {0} sleeps for {1} senconds.".format(name,i))
	time.sleep(i)
	print("Thread {0} woke up.".format(name))

if __name__ == '__main__':
	t1 = Thread(target = sleep, args=("Thread 1", 3))
	t2 = Thread(target = sleep, args=("Thread 2", 7))
	t1.start()
	t2.start()
