# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 18:58:05
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:24:02
# @Title: Program to add leading zeroes to a string


str1='150.35'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0') # left align the string
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='150.35'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)