# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day11-6
   Description :   读取json文件
   Author :        Robert Xu
   date：          2020/1/26
-------------------------------------------------
   Change Activity:
                   2020/1/26:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

import json


def main():
    mydict = {
        'name': 'Robert Xu',
        'age': 38,
        'qq': 12345,
        'friends': ['Robert', 'Richard'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('test.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')


if __name__ == '__main__':
    main()
