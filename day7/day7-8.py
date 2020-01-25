# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day7-8.py
   Description :   list3
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

# 列表切片
fruits2 = fruits[1:4]
print(fruits2)  # ['apple', 'strawberry', 'waxberry']
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
