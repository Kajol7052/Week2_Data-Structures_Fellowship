# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 16:17:52
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 16:29:29
# @Title: Program to remove a key from a dictionary


number = int(input("Enter a number: "))
square_dict = dict()

for x in range(1, number+1):
    square_dict.update({x:x*x})
    # square_dict[x] = x*x
print("Before removing Key, Dictionary is: ", square_dict) 

key = (int(input("Enter the key to remove: ")))
if key in square_dict:
    del square_dict[key] # delete a key from the dictionary
print("After removing Key, Dictionary is: ", square_dict)