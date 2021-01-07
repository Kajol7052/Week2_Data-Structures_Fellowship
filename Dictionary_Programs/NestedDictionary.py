# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 19:06:18
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 19:55:05
# @Title: Program to convert a list into a nested dictionary of keys


num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)