# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day5-pra3.py
   Description :  输出100以内所有的素数。
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

from math import sqrt

for i in range(1, 101):
    end = int(sqrt(i))
    is_prime = True
    for x in range(2, end + 1):
        if i % x == 0:
            is_prime = False
            break
    if is_prime and i != 1:
        print('%d是素数' % i)
