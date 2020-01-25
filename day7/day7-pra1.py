# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day7-pra1
   Description :   在屏幕上显示跑马灯文字
   Author :        Robert Xu
   date：          2020/1/25
-------------------------------------------------
   Change Activity:
                   2020/1/25:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

import os
import time


def main():
    content = '北京欢迎你为你开天辟地.......'
    while True:
        # 清理屏幕上的输出
        os.system('clear')
        print(content)
        # sleep 200 ms
        time.sleep(1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
