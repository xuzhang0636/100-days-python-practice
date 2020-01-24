# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day6-2.py
   Description :   refactor day6-1.py
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

from math import factorial

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))
