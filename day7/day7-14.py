# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     day7-14
   Description :   字典
   Author :        Robert Xu
   date：          2020/1/25
-------------------------------------------------
   Change Activity:
                   2020/1/25:
-------------------------------------------------
"""
__author__ = 'Robert Xu'

# 创建字典的字面量语法
scores = {'Robert Xu': 95, 'Richard Xu': 92, 'dd': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=2, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通过键可以获取字典中对应的值
print(scores['Robert Xu'])
print(scores['Richard Xu'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['Robert Xu'] = 65
scores['tt'] = 71
scores.update(李元芳=34, 狄仁杰=88)
print(scores)
if '秦始皇' in scores:
    print(scores['秦始皇'])
print(scores.get('秦始皇'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('秦始皇'), 12)
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
# 如果key值存在，弹出对应的值，否则弹出默认值
print(scores.pop('Robert Xu1', 100))
# 清空字典
scores.clear()
print(scores)
