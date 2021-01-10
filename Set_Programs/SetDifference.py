# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:49:56
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:56:56
# @Title: Program to create difference of sets


class DiffSet:
    def create_difference(self):
        my_set = set()
        size = int(input("Enter the size of the set: "))
        num = 0
        while num<size:
            my_set.add(int(input("Enter the unique elements in set: ")))
            num+=1
        return my_set

set_1 = set_2 = set()
diffSet = DiffSet()
set_1 = diffSet.create_difference()
set_2 = diffSet.create_difference()
print("Set 1 is: ", set_1)
print("Set 2 is: ", set_2)
print("Difference of the Set_1 - Set_2 is:  ", set_1.difference(set_2))
print("Difference of the Set_2 - Set_1 is:  ", set_2.difference(set_1))
print(diffSet.create_difference.__doc__)
