# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:46:24
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:50:37
# @Title: Program to iteration over sets


class CreateSet:
    def addElement(self,my_set,size):
        for i in range(size):   # loop to insert items in set
            my_set.add(int(input("Enter the unique elements in set: ")))
        return my_set
my_set = set()
size = (int(input("Enter the size of the set: ")))
creator = CreateSet()
my_set = creator.addElement(my_set,size)
print("Set elements are: ")
for x in my_set:    # loop to iterate over set
    print(x,end=' ')
print()
print(creator.addElement.__doc__)