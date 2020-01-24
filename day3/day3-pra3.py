"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: Robert Xu
"""

first_edge = float(input('请输入第一条边的长度：'))
second_edge = float(input('请输入第二条边的长度：'))
third_edge = float(input('请输入第三条边的长度：'))

if first_edge + second_edge > third_edge and first_edge + third_edge > second_edge and second_edge + third_edge > first_edge:
    print('周长：', first_edge + second_edge + third_edge)
    p = (first_edge + second_edge + third_edge) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：', area)
else:
    print("不能构成三角形")
