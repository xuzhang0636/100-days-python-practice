# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day11-2
   Description :   读文件2
   Author :        Robert Xu
   date：          2020/1/26
-------------------------------------------------
   Change Activity:
                   2020/1/26:
-------------------------------------------------
"""
__author__ = 'Robert Xu'


def main():
    try:
        with open('test.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未开的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')


if __name__ == '__main__':
    main()
