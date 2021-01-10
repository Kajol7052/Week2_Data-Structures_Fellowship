# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:09:05
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:32:37
# @Title: Program to determine if the python shell is executing in 32bit or 64bit mode on operating system

# For 32 bit it will return 32 and for 64 bit it will return 64
# The struct module in Python is used to convert native Python data types such as strings and numbers into a string of bytes and vice versa.
import struct

print(struct.calcsize("P") * 8) # returns the size of bytes required to store a single pointer