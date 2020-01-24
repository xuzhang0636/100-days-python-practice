# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day7-11.py
   Description :   生成器yield斐波那契数列
   Author :        Robert Xu
   date：          2020/1/24
-------------------------------------------------
   Change Activity:
                   2020/1/24:
-------------------------------------------------
"""
__author__ = 'Robert Xu'


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
