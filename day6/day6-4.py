# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day6-4.py
   Description :
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'


# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或者多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 5, 7, 9))
