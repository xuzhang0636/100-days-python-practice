# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day7-pra7
   Description :   双色球选号
   Author :        Robert Xu
   date：          2020/1/25
-------------------------------------------------
   Change Activity:
                   2020/1/25:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    :param balls:
    :return:
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    :return:
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()