# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-04 19:07:33
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-04 19:47:07
# @Title: Accepts a sequence of numbers from user and generate a list and a tuple with those numbers.

# function to generate list and tuple
def list_tuple():
    values = input("Enter some comma seperated values: ")
    lists = values.split(",")
    tuples = tuple(lists)
    print("List: ", lists)
    print("Tuple: ", tuples)

list_tuple()