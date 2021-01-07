# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 15:11:30
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:35:45
# @Title: Program to Sort (ascending and descending) a Dictionary by value

class Dictionary:
    def sort(self,input_dict):
        asc_order = sorted(input_dict.items(), key=lambda x: x[1])
        for i in asc_order:
            asc = dict(asc_order)
        print("Ascending order is: ", asc)

        # Sort the Dictionary in descending order by value   
        desc_order = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)
        for i in desc_order:
            desc = dict(desc_order)
        print("Descending order is: ", desc)

input_dict = {'alan':30,'danny':10,'carl':20,'bob':40} 

# sorted() func can be used to sort iterable objects by a key, such as lists, tuples, and dictionaries. 
# The sorted() function sorts the items of the specified iterable object and creates a new object with the newly sorted values.
# Sort the Dictionary in ascending order by value
dictionary = Dictionary()
dictionary.sort(input_dict)
print(dictionary.sort.__doc__)