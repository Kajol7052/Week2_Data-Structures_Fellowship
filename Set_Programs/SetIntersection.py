# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:50:03
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:58:25
# @Title: Program to create an Intersection of the Sets

class IntSet:
    def create_intersection(self):
        my_set = set()
        size = int(input("Enter the size of the set: "))
        num = 0
        while num<size:
            my_set.add(int(input("Enter the unique elements in set: ")))
            num+=1
        return my_set


set_1 = set_2 = set()
intSet  = IntSet()
set_1 = intSet.create_intersection()
set_2 = intSet.create_intersection()
print("Set 1 is: ", set_1)
print("Set 2 is: ", set_2)
print("Intersection of the Sets is: ", set_1.intersection(set_2))
print(intSet.create_intersection.__doc__)
