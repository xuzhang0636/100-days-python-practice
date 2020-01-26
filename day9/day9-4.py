# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day9-4.py
   Description :   classmethod
   Author :        Robert Xu
   date：          2020/1/25
-------------------------------------------------
   Change Activity:
                   2020/1/25:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        current_time = localtime(time())
        return cls(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02s' % (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
