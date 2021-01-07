# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:49:45
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:52:43
# @Title: Program to remove the items from the set if present


class ElementRemover:

    def remove_element_if_present(self,new_set, ele):
        if ele in new_set:
            new_set.remove(ele)
            print("Successfully removed",ele,"from the set")
        else:
            print("Element is not present in the set")
        return new_set

my_set = set()
size = (int(input("Enter the size of the set: ")))
for i in range(size):
    my_set.add(int(input("Enter the unique elements in set: ")))
print("Before removing the element: ", my_set)

element = (int(input("Enter the element to remove from the set: ")))
elementRemover = ElementRemover()
print("After removing the element: ", elementRemover.remove_element_if_present(my_set,element))
print(elementRemover.remove_element_if_present.__doc__)