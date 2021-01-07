# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 22:20:29
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 01:11:24
# @Title: Program to slice a tuple

import CustomExceptions
try:
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    print(my_tuple[2:7])
    print(my_tuple[7:7])
    print(my_tuple[:5])
    print(my_tuple[4:])
    print(my_tuple[-9:-5])
    print(my_tuple[:-1])
    print(my_tuple[:])
    print()
    my_tuple1 = tuple("HELLO WORLD")
    print(my_tuple1)
    print(my_tuple1[2:9:2])
    print(my_tuple1[::4])
except CustomExceptions.IndexError:
    print("Index error found")
