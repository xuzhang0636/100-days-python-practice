# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day4-2
   Description :   才数组游戏，计算机出一个1～100之间的随机数字由人来猜，计算机根据人猜测分别给出提示大一点/小一点/猜对了
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

import random

counter = 0
answer = random.randint(1, 100)
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        break

if counter > 7:
    print('您的智商有待提高！！')

