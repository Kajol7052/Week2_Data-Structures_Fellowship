# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:27
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:33:49
# @Title: Pprogram to convert an integer to binary keep leading zeros

x = int(input("Enter decimal number to convert into binary: "))
print(format(x, '08b'))
print(format(x, '010b'))