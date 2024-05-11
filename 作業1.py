#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:27:19 2024

@author: mac
"""

import random

# 创建一个集合来存储生成的数
random_numbers = set()

# 循环生成5个满足条件的数
while len(random_numbers) < 5:
    num = random.randint(5, 100)
    if num % 5 == 0:
        random_numbers.add(num)

# 使用5个变量来储存生成的数
num1, num2, num3, num4, num5 = random_numbers

print("生成的5个满足条件的数：", num1, num2, num3, num4, num5)