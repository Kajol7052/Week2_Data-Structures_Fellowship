# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:05:12
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 21:18:17
# @Title: Program to get numbers divisible by fifteen from a list using an anonymous function


number_list = [45, 55, 60, 30, 35, 100, 105, 220]
# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
result = list(filter(lambda x: (x % 15 == 0), number_list))
print("Numbers divisible by 15 are", result)