# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:04:52
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:05:06
# @Title: Print out a set containing all the colors from color_list_1 which are not present in color_list_2.


color_list1 = set(["White", "Black", "Red"])
color_list2 = set(["Red", "Green"])

print(color_list1.difference(color_list2))
print(color_list2.difference(color_list1))
