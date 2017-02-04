#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

# lambda function to find out the maximum
max = lambda x, y: x if x > y else y

if __name__ == '__main__':
    # list example
    list = [12, 34, 1, 45, 78, 132]

    print(functools.reduce(max, list))
