# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:50
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:01:06
# @Title: Program to get the size of an object in bytes


import sys

str1 = "Kajol"
str2 = "Hello, World!"
str3 = "OOPS"
print()
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
print()
