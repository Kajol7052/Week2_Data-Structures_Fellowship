# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 14:59:17
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:36:05
# @Title: Program to Sort (ascending and descending) a Dictionary by key
class Dictionary:
    def sort(self,input_dict):
        asc = list(input_dict.items())   # convet the given dict into list and In Python Dictionary, items() method is used to return the list with all dictionary keys with values.
        asc.sort()                      # sort the list
        dict_asc = dict(asc)           # sort the list
        print('Ascending order is: ',dict_asc) # print the sorted dict in ascending order 
        # Sort the Dictionary in Ascending order by Key
        desc =list(input_dict.items())
        desc.sort(reverse=True)        # sort the list in reverse order
        dict_desc = dict(desc)
        print('Descending order is: ',dict_desc)

input_dict = {'carl':10,'alan':30,'bob':40,'danny':20} 
dictionary = Dictionary()
dictionary.sort(input_dict)
print(dictionary.sort.__doc__)
