# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:46:27
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:36:10
# @Title: Program to add elements in a set



class AddElement:
    def add_element(self, new_set, ele):
        '''
        This method is used to add an element
        to a given Set.
        '''
        new_set.add(ele)
        return new_set
my_set = set()
size = int(input("Enter the size of the set: "))
for i in range(size):
    my_set.add(int(input("Enter the unique elements in set: ")))
print("Before adding the element: ", my_set)

caller = AddElement() # object instantiated
element = int(input("Enter the element to add in the set: "))
print("After adding the element: ", caller.add_element(my_set,element))
print(caller.add_element.__doc__)
