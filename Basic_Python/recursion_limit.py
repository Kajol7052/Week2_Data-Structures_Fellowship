# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:58
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:02:27
# @Title: Program to get the current value of the recursion limit


#   Python's default recursion limit is 1000, meaning that Python won't let a function call on itself more than 1000 times, 
#   which for most people is probably enough. The limit exists because allowing recursion to occur more than 1000 times doesn't exactly make for lightweight code.
import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()