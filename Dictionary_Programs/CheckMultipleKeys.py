# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 19:57:24
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-06 10:05:10
# @Title: Program to check multiple keys exists in a dictionary. 

student = {"name":"Kajol", "course":"BE", "year":4, "fee":100000}
key_set1 = {"name","course"}
key_set2 = {"year","id"}
print(student.keys() >= key_set1) # keys() return a view object(this view oject contains the key of the dictionary as a list)
print(student.keys() >= key_set2)