# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:46:22
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:55:26
# @Title: Program to remove Items from the Set


class ElementRemover:

    def removeElement(self,new_set, ele):
        new_set.remove(ele)
        return new_set

my_set = set()
size = (int(input("Enter the size of the set: ")))
for i in range(size):
    my_set.add(int(input("Enter the unique elements in set: ")))
print("Before removing the element: ", my_set)

element = (int(input("Enter the element to remove from the set: ")))
elementRemover = ElementRemover()
print("After removing the element: ", elementRemover.removeElement(my_set,element))
print(elementRemover.removeElement.__doc__)