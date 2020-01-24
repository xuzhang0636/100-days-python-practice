# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day5-pra1.py
   Description :  生成斐波那契数列的前20个数
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

a = 1
b = 1
print(a)
print(b)
for x in range(18):
    c = a + b
    print(c)
    a, b = b, c
