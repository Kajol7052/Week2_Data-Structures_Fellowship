# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-05 20:19:32
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-05 22:42:42
# @Title: Program to create a set

class SetCreate:

    def createSet(self,size):

        my_set = set()
        for i in range(size):
            my_set.add(int(input("Enter the unique elements in set: ")))
        return my_set

size=(int(input("Enter the size of the set: ")))
#loop to insert items in set
setCreate = SetCreate()
my_set = setCreate.createSet(size)
print(setCreate.createSet.__doc__)
print("Created Set is: ", my_set)