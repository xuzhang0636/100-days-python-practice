# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day-pra2.py
   Description :   输入两个正整数计算他们的最大公约数和最小公倍数
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
