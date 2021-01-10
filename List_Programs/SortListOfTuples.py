# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-06 18:06:17
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-08 09:57:35
# @Title: Program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


# take the second element for sort
def second_element(element):
    return element[1]


# list
my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(my_list, key=second_element) # sort list with key(that is value here)
print('Sorted list:', sorted_list)  # print list