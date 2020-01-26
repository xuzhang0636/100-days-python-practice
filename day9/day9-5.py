# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day9-5.py
   Description :   继承和多态
   Author :        Robert Xu
   date：          2020/1/25
-------------------------------------------------
   Change Activity:
                   2020/1/25:
-------------------------------------------------
"""
__author__ = 'Robert Xu'


class Person(object):
    """人"""

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
        print('%s正在愉快的玩耍。' % self._name)

    def watch_av(self):
        if self.age >= 18:
            print('%s正在观看动作片.' % self._name)
        else:
            print('%s正在观看熊出没' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s' % (self._name, self._title, course))


def main():
    stu = Student('Robert Xu', 30, '高3')
    stu.study('计算机')
    stu.watch_av()
    t = Teacher('Richard Xu', 30, '教授')
    t.teach('Java')
    t.watch_av()


if __name__ == '__main__':
    main()
