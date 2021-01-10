# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:49:37
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:45:30
# @Title: Program to use Frozen Sets


class SetCreator:
    def create_set(self):
        my_set=set()
        size=(int(input("Enter the size of the set: ")))
        for i in range(size):
            my_set.add(int(input("Enter the unique elements in set: ")))
        return my_set

    def add_element(self,mySet,value):
        try:
            mySet.add(value)
        except:
            print("You cannot add element in this set becaues it is forzen set")
        return mySet

creator = SetCreator()
set_1 = creator.create_set()
set_2 = frozenset(creator.create_set()) #function call to create set ,converts normal list to frozen list and assigns to set 2

print("Before adding the element: ")
print("Set 1 is: ",set_1)
element = (int(input("Enter the element to add in the set: ")))
set_1 = creator.add_element(set_1, element)
print("After adding the element: ",set_1)

print("Before adding the element: ")
print("Set 2 is: ",set_2)
element = (int(input("Enter the element to add in the set: ")))
set_2 = creator.add_element(set_2, element)
print("After adding the element: ",set_2)
print(creator.create_set.__doc__)
print(creator.add_element.__doc__)