#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:32:02 2024

@author: mac
"""

def is_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True

# 获取用户输入的边长
a = float(input("请输入第一条边的长度："))
b = float(input("请输入第二条边的长度："))
c = float(input("请输入第三条边的长度："))

# 验证是否构成三角形
if is_triangle(a, b, c):
    print("可以构成三角形。")
else:
    print("不能构成三角形。")