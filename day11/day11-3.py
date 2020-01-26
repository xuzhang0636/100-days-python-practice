# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day11-3
   Description :
   Author :        Robert Xu
   date：          2020/1/26
-------------------------------------------------
   Change Activity:
                   2020/1/26:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

import time


def main():
    # 一次性读取真个文件内容
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    # 通过for-in循环逐行读取
    with open('test.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('test.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
