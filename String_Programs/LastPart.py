# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-07 20:13:30
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-07 23:19:51
# @Title: Program to get the last part of a string before a specified character
#   Input:  https://www.w3resource.com/python-exercises
#	Output: https://www.w3resource.com/python
import CustomExceptions

try:
    my_str = input("Enter a string: ")
    print(my_str.rsplit('/', 1)[0])
    print(my_str.rsplit('-', 1)[0])
    print (my_str.rpartition('-')[0])


    str1 = 'https://www.w3resource.com/python-exercises'
    print(str1)
    char=input("Enter any character from above string: ")
    for subString in str1.split(char):
        print(subString)
        break
except CustomExceptions.Error:
    print("Error Occured")