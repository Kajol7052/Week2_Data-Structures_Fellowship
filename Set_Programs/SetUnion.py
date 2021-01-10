# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:50:08
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:59:41
# @Title: Program to create Union of sets


class UnionSet:
    def create_union(self):
        my_set = set()
        size = int(input("Enter the size of the set: "))
        num = 0
        while num<size:
            my_set.add(int(input("Enter the unique elements in set: ")))
            num+=1
        return my_set

set_1 = set_2 = set()
unionSet = UnionSet()
set_1 = unionSet.create_union()
set_2 = unionSet.create_union()
print("Set 1 is: ", set_1)
print("Set 2 is: ", set_2)
print("Union of the Sets is: ", set_1.union(set_2))
print(unionSet.create_union.__doc__)
