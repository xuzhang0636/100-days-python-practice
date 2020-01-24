# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day7-12.py
   Description :   tuple1
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'
# define tuple,元组中的数据不能修改
t = ('Robert xu', 30, True, 'Xi\'an')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = 'ttt' # TypeError
# 变量t重新引用了新的元组，原来的元组将被垃圾回收
t = ('Richard xu', 20, False, 'chongqing')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 将列表转换成元组
fruits_lit = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_lit)
print(fruits_tuple)
