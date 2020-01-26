# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day10-1
   Description :
   Author :        Robert Xu
   date：          2020/1/26
-------------------------------------------------
   Change Activity:
                   2020/1/26:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

"""
使用tkinter开发GUI应用需要以下5个步骤：
1.导入tkinter模块中我们需要的东西
2.创建一个顶层窗口对象并用它来承载整个GUI应用
3.在顶层窗口对象上添加GUI组件
4.通过代码将这些GUI组件的功能组织起来
5.进入主事件循环
"""

import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改便签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '你确定要退出吗？'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
