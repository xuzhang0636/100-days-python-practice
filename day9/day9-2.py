# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day9-2.py
   Description :   __slots__魔法
   Author :        Robert Xu
   date：          2020/1/25
-------------------------------------------------
   Change Activity:
                   2020/1/25:
-------------------------------------------------
"""
__author__ = 'Robert Xu'


class Person(object):
    # 限定Person对象只能绑定_name,_age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self.age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('Robert Xu', 30)
    person.play()
    person._gender = '男'
    # person.is_gay = True


if __name__ == '__main__':
    main()
