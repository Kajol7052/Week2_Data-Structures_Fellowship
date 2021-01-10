# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:04:11
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 20:03:39
# @Title: Concatenate all elements in a list into a string and return it

# function to concatenate list into string
def concatenate_list(lists):
    result = ''
    for element in lists:
        result += str(element)
    return result

print("Concatenated String is: ", concatenate_list([11, 12, 13, 14]))
print("Concatenated String is: ",concatenate_list([1, 0, 0, 11]))