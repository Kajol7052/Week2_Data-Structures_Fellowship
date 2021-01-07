# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:50:15
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 23:01:44
# @Title: Program to create a symmetric difference from sets


class DiffSym:
    def symmetric_difference(self):
        my_set = set()
        size = int(input("Enter the size of the set: "))
        num = 0
        while num<size:
            my_set.add(int(input("Enter the unique elements in set: ")))
            num+=1
        return my_set

set_1 = set_2 = set()
diffSym = DiffSym()
set_1 = diffSym.symmetric_difference()
set_2 = diffSym.symmetric_difference()
print("Set 1 is: ", set_1)
print("Set 2 is: ", set_2)
print("Difference of the Set_1 - Set_2 is:  ", set_1.symmetric_difference(set_2))
print(diffSym.symmetric_difference.__doc__)
