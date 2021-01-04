# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:06:29
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:35:31
# @Title: Program to extract single key-value pair of a dictionary in variables


d = {'Color': 'Blue'}
(key, value), = d.items()
print(key)
print(value)
