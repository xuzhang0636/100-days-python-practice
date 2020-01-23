"""
练习2：百分制成绩转换为等级制成绩。

Version: 0.1
Author: Robert Xu
"""

score = int(input('请输入成绩：'))

if score >= 90:
    result = 'A'
elif score >= 80 and score < 90:
    result = 'B'
elif score >= 70 and score < 80:
    result = 'C'
elif score >= 60 and score < 70:
    result = 'D'
else:
    result = 'E'

print('成绩是：', result)
