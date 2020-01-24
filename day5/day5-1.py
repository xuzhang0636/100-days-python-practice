# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day5-1.py
   Description :   寻找水仙花数, 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

number = int(input('请输入一个三位数:'))

first = number // 100
second = number % 100 // 10
third = number % 10
if number == first ** 3 + second ** 3 + third ** 3:
    print("是")
else:
    print("否")
