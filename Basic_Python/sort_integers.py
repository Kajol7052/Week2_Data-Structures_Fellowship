# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:09:29
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:52:56
# @Title: Program to sort three integers without using conditional statements and loops.

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)
