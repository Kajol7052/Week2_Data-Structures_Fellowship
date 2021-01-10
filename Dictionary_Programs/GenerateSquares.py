# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 16:10:58
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 16:17:18
# @Title: Program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

number = int(input("Enter a number: "))
square_dict = dict()

for x in range(1, number+1):
    square_dict.update({x:x*x})
    # square_dict[x] = x*x

print("Dictionary is: ", square_dict) 
