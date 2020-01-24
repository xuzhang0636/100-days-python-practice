# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day4-2
   Description :    用for循环实现1~100之间的偶数求和
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

# Solution1
sum = 0
for i in range(2, 101, 2):
    sum += i
print('Solution 1:1~100之间的偶数和：', sum)

# Solution2
result = 0
for i in range(101):
    if i % 2 == 0:
        result += i
print('Solution 2:1~100之间的偶数和：', result)
