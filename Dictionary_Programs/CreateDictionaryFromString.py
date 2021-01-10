# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 18:44:33
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-06 10:13:02
# @Title: Program to create a dictionary from a string

input_string = 'w3resource'
new_dict = {}
for char in input_string:
    new_dict[char] = new_dict.get(char, 0) + 1 # get() method returns the value of the item with the specified key.
print("The dictionary created is: ",new_dict)

