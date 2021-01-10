# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 18:58:36
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 19:58:36
# @Title: Check whether a specified value is contained in a group of values

# function to check value is present or not
def check_value_present_or_not(list_element,element):
    for value in list_element:
        if element == value: # checking value is present or not
            return True
    return False
    
print(check_value_present_or_not([1, 5, 8, 3], 3))
print(check_value_present_or_not([1,5, 8, 3], -1))